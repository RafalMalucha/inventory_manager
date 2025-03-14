import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  plugins: [vue()],
  server: {
    host: "0.0.0.0",
    port: 5173,
    strictPort: true, 
    watch: {
      usePolling: true, 
    },
    proxy: {
      "/api": "http://127.0.0.1:8000", // Proxy FastAPI backend
    },
  },
});