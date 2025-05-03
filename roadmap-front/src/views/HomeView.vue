<template>
  <div class="main">
    <h1>Предметы</h1>

    <div class="cards">
      <button
        v-for="(item, idx) in subjects"
        :key="idx"
        type="button"
        class="card"
        @click="onCardClick(item)"
      >
        <h2 class="card-title">{{ item.title }}</h2>
        <p class="card-teacher">{{ item.teacher }}</p>
        <p class="card-duration">{{ item.duration }}</p>
        <div class="progress">
          <div class="progress-fill" :style="{ width: item.progress + '%' }"></div>
        </div>
        <span class="progress-text">{{ item.progress }}%</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const subjects = ref([
  { title: 'ООП и алгоритмы',       teacher: 'Иванов И.',    duration: '12 недель', progress: 60 },
  { title: 'Дискретная математика', teacher: 'Кукушкина М.', duration: '12 недель', progress: 80 },
  { title: 'BackEnd and Data',      teacher: 'Тодов Ю.',     duration: '12 недель', progress: 74 },
])

function onCardClick(item) {
  // здесь можно обработать клик по карточке
  console.log('Клик по предмету:', item.title)
}
</script>

<style scoped>
.main {
  padding: 20px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.cards {
  display: flex;
  gap: 16px;
  margin-top: 20px;
}
/* Сброс стандартных стилей кнопки и добавление стилей карточки */
button.card {
  all: unset;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  flex: 1;
  border: 2px solid #795ef5;
  border-radius: 8px;
  padding: 16px;
  text-align: left;
  transition: box-shadow 0.2s;
}
button.card:hover {
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}

.card-title {
  margin: 0 0 8px;
  font-size: 1.1rem;
}
.card-teacher,
.card-duration {
  margin: 0;
  color: #555;
  font-size: 0.9rem;
}
.progress {
  background: #eee;
  height: 10px;
  border-radius: 4px;
  overflow: hidden;
  margin: 12px 0 4px;
}
.progress-fill {
  background: #43d7b6;
  height: 100%;
}
.progress-text {
  font-size: 0.9rem;
  font-weight: bold;
  color: #333;
}
</style>
