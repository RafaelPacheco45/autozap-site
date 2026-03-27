const { generateResponse } = require("./response_engine");

async function handleMessage(message, client, config) {
    const texto = message.body.trim();

    console.log(`📩 ${message.from}: ${texto}`);

    const resposta = await generateResponse(texto, config);

    if (resposta) {
        await client.sendMessage(message.from, resposta);
    }
}

module.exports = { handleMessage };
