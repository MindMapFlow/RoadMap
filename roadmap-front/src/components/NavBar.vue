<template>
  <nav class="navbar">
    <div class="navbar-logo">
      <img src="@/assets/logo.png" alt="Logo">
    </div>
    <ul class="navbar-menu">
      <li><a href="/">Главная</a></li>
      <li><a href="/roadmap">Карта</a></li>
      <li><a href="#">Материалы</a></li>
    </ul>
    <div class="navbar-search">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-search">
        <circle cx="11" cy="11" r="8"></circle>
        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
      </svg>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 10px 20px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);

}

.navbar-logo {
  display: flex;
  align-items: center;
}

.navbar-logo img {
  width: auto;
  height:100px;
  margin-right: 10px;
}


.navbar-menu {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 10px;
}

.navbar-menu li {
  margin-left: 20px;
  transition: background-color 0.3s ease;
  padding: 15px;
  border-radius: 20px;
  background-color: #5656D6;
}

.navbar-menu a {
  color: #ffffff;
  padding: 5px 10px;
  font-size: 20px;
}

.navbar-menu li:hover {
  background: #d3e0f0;
  color: #5656D6;
  text-decoration: none;
}
.navbar-menu li a:hover {
  color: #5656D6;
  text-decoration: none;
}

.navbar-search {
  margin-left: 20px;
}
.navbar-search svg {
  width: 35px;
  height: 35px;
  color: #5656D6;
  cursor: pointer;
}
</style>