import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'node:path'


export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, path.resolve(__dirname), 'VITE_') // only frontend/.env*
  const target = env.VITE_API_BASE
  console.log('Vite mode:', mode)
  console.log('target:', target)

  return {
    plugins: [vue()],
    server: {
      host: '0.0.0.0',
      port: 5173,
      proxy: {
        '/api': { target: target, changeOrigin: true },
      },
    },
  }
})
