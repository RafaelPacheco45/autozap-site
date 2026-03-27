const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const axios = require("axios");
const fs = require("fs");
const path = require("path");

const app = express();
app.use(cors());
app.use(bodyParser.json());

const PORT = 3000;
const MP_TOKEN = "APP_USR-2439733670232749-032710-143a893b8b974959ce45e84ad8352cc7-3297249488";

const dataDir = path.join(__dirname, "data");
const CLIENTS_FILE = path.join(dataDir, "clients.json");

// garante pasta e arquivo
if (!fs.existsSync(dataDir)) {
  fs.mkdirSync(dataDir, { recursive: true });
}

if (!fs.existsSync(CLIENTS_FILE)) {
  fs.writeFileSync(CLIENTS_FILE, "[]", "utf8");
}

function loadClients() {
  try {
    const raw = fs.readFileSync(CLIENTS_FILE, "utf8");
    return JSON.parse(raw || "[]");
  } catch (err) {
    console.error("Erro ao carregar clients.json:", err.message);
    return [];
  }
}

function saveClients(clients) {
  try {
    fs.writeFileSync(CLIENTS_FILE, JSON.stringify(clients, null, 2), "utf8");
    console.log("clients.json salvo com sucesso em:", CLIENTS_FILE);
  } catch (err) {
    console.error("Erro ao salvar clients.json:", err.message);
  }
}

app.get("/", (req, res) => {
  res.send("Backend AutoZap rodando.");
});

app.get("/clients", (req, res) => {
  const clients = loadClients();
  res.json(clients);
});

app.post("/create-checkout", async (req, res) => {
  try {
    const data = req.body;

    console.log("Novo cadastro recebido:", data);

    const priceMap = {
      "Plano Básico": 50,
      "Plano Intermediário": 100,
      "Plano Avançado": 200
    };

    const price = priceMap[data.plano];

    if (!price) {
      return res.status(400).json({ error: "Plano inválido" });
    }

    const clients = loadClients();

    const newClient = {
      id: Date.now(),
      nome: data.nome || "",
      telefone: data.telefone || "",
      email: data.email || "",
      senha: data.senha || "",
      loja: data.loja || "",
      responsavel: data.responsavel || "",
      endereco: data.endereco || "",
      nicho: data.nicho || "",
      plano: data.plano || "",
      descricao: data.descricao || "",
      price,
      status_pagamento: "pendente",
      status_licenca: "inativa",
      created_at: new Date().toISOString()
    };

    clients.push(newClient);
    saveClients(clients);

    console.log("Cliente salvo no JSON:", newClient);

    const payment = await axios.post(
      "https://api.mercadopago.com/checkout/preferences",
      {
        items: [
          {
            title: `AutoZap - ${data.plano}`,
            quantity: 1,
            unit_price: price
          }
        ],
        payer: {
          name: data.nome,
          email: data.email
        }
      },
      {
        headers: {
          Authorization: `Bearer ${MP_TOKEN}`,
          "Content-Type": "application/json"
        }
      }
    );

    res.json({
      checkout_url: payment.data.init_point
    });
  } catch (err) {
    console.error("Erro ao criar checkout:");
    console.error(err.response?.data || err.message);

    res.status(500).json({
      error: "Erro ao criar pagamento"
    });
  }
});

app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});