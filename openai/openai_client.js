const OpenAI = require("openai");
const { buildPrompt } = require("./prompt_builder");

async function askOpenAI(message, config) {
    const openai = new OpenAI({
        apiKey: config.openai_key
    });

    const systemPrompt = buildPrompt(config);

    const response = await openai.chat.completions.create({
        model: "gpt-4o-mini",
        messages: [
            {
                role: "system",
                content: systemPrompt
            },
            {
                role: "user",
                content: message
            }
        ],
        temperature: 0.7
    });

    return response.choices[0].message.content;
}

module.exports = { askOpenAI };