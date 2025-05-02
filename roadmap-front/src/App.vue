<template>
  <div class="app-wrapper">
    <NavBar />
    <router-view class="main-content" />
    <Footer />
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import Footer from './components/FooterPage.vue'

export default {
  components: {
    NavBar,
    Footer
  }
}
</script>

<style scoped>
.app-wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content {
  flex: 1;
  padding-bottom: 20px;
}


</style>