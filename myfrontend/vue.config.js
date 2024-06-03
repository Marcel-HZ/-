module.exports = {
    publicPath: "./",
    outputDir: "dist",
    assetsDir:"static",
    devServer: {
        proxy: {
            '/api': {
                target: 'http://localhost:5000',
                changeOrigin: true,
                pathRewrite: {
                    '^/api': '',
                },
            },
        },
    },
};