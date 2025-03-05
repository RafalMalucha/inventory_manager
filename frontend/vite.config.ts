import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 5173, // Set a fixed port
    strictPort: true, // Prevent switching to the next port
    proxy: {
      "/api": "http://127.0.0.1:8000", // Proxy FastAPI backend
    },
  },
});