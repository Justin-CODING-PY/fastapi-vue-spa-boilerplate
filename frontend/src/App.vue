<script setup lang="ts">
import { ref, onMounted } from 'vue'

const msg = ref('loading...')
onMounted(async () => {
  try {
    const r = await fetch('/api/v1/health')
    if (!r.ok) throw new Error(`${r.status} ${r.statusText}`)
    msg.value = JSON.stringify(await r.json())
  } catch (e:any) {
    msg.value = `error: ${e.message}`
  }
})
</script>

<template>
  <main style="padding:2rem;font-family:sans-serif">
    <h1>Django + Vue</h1>
    <p>Health: {{ msg }}</p>
  </main>
</template>
