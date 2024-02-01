import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      // 配置代理，以便在开发中将API请求代理到Flask服务器
      '/api': {
        target: 'http://localhost:5000', // Flask后端服务器地址
        changeOrigin: true,
        secure: false,
        ws: true,
      },
    },
  },
  build: {
    outDir: 'dist', // 构建输出目录
    emptyOutDir: true, // 构建前清空输出目录
    rollupOptions: {
      // 配置Rollup选项来控制构建输出
      input: {
        main: "./index.html"
        // 如果有其他的入口点，可以在这里添加
      },
      output: {
        // 输出配置，根据需要进行调整
        chunkFileNames: 'index.html',
        entryFileNames: 'main.js',
        assetFileNames: 'static/style.css',
      },
    },
  },
})
