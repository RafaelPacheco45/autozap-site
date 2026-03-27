const { askOpenAI } = require("../openai/openai_client");

async function generateResponse(texto, config) {
    if (!config.use_ai) {
        if (texto.toLowerCase() === "oi") {
            return "Olá! Como posso te ajudar?";
        }
        return null;
    }

    return await askOpenAI(texto, config);
}

module.exports = { generateResponse };
