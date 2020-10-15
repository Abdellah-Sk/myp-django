const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    entry: path.resolve(__dirname, "src/projects/static/projects/dev/index.js"),
    output: {
        filename: "bundle.js",
        path: path.resolve(__dirname, "src/projects/static/projects/dist")
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: '[name].css',
            chunkFilename: '[id].css',
        })
    ],
    module: {
        rules: [{
            test: /\.scss$/,
            use: [
                MiniCssExtractPlugin.loader, // 3. Recrée les fichiers css à partir de leurs équivalents en Javascript.
                "css-loader", // 2. Converti les fichiers CSS en équivalents Javascript
                "sass-loader" // 1. Transpile le SCSS en CSS
            ],
            exclude: /node_modules/
        }]
    }
};