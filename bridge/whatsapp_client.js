const { Client, LocalAuth } = require("whatsapp-web.js");
const qrcode = require("qrcode-terminal");
const { handleMessage } = require("../core/message_router");

function startWhatsApp(config) {
    const client = new Client({
        authStrategy: new LocalAuth()
    });

    client.on("qr", (qr) => {
        console.log("📱 Escaneia o QR abaixo:");
        qrcode.generate(qr, { small: true });
    });

    client.on("ready", () => {
        console.log("✅ WhatsApp conectado com sucesso.");
    });

    client.on("message", async (message) => {
        await handleMessage(message, client, config);
    });

    client.initialize();
}

module.exports = { startWhatsApp };
