const { loadConfig } = require("./init_config");
const { startWhatsApp } = require("../bridge/whatsapp_client");

async function startApp() {
    const config = loadConfig();
    console.log("🚀 Iniciando AutoZap...");
    startWhatsApp(config);
}

startApp();
