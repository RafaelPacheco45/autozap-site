const fs = require("fs");
const path = require("path");

function loadConfig() {
    const userConfigPath = path.join(__dirname, "../config/user_config.json");
    const defaultConfigPath = path.join(__dirname, "../config/default.json");

    const defaultConfig = JSON.parse(fs.readFileSync(defaultConfigPath, "utf8"));

    if (!fs.existsSync(userConfigPath)) {
        return defaultConfig;
    }

    const userConfig = JSON.parse(fs.readFileSync(userConfigPath, "utf8"));
    return { ...defaultConfig, ...userConfig };
}

module.exports = { loadConfig };
