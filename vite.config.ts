import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import alias from '@rollup/plugin-alias';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        secure: false,
        ws: true,
      },
    },
  },
  build: {
    outDir: 'src/templates',
    emptyOutDir: true,
    rollupOptions: {
      input: "./index.html",
      output: {
        entryFileNames: "static/index.js",
        assetFileNames: "static/style.css",
        chunkFileNames: "index.html"
      },
    }
  }
})
