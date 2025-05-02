<template>
  <VueFlow :nodes="nodes" :edges="edges" fit-view class="roadmap-flow" @node-click="handleNodeClick" />

  <div v-if="selectedNode" class="node-description">
    <button class="close-button" @click="selectedNode = null">×</button>
    <h3>{{ selectedNode.label }}</h3>
    <p>{{ selectedNode.description }}</p>
    <iframe
        v-if="selectedNode.video"
        width="100%"
        height="215"
        :src="selectedNode.video"
        frameborder="0"
        allowfullscreen
    ></iframe>
    <p><strong>Дополнительные материалы:</strong></p>
    <a :href="selectedNode.material" target="_blank">{{ selectedNode.material }}</a>
    <p v-if="selectedNode.assignment"><strong>Задание:</strong> {{ selectedNode.assignment }}</p>
  </div>
</template>

<script setup>
import '@vue-flow/core/dist/style.css'
import {VueFlow} from '@vue-flow/core'
import {ref} from 'vue'

const selectedNode = ref(null)

const handleNodeClick = (event) => {
  const nodeId = event.node.id
  const node = nodes.find(n => n.id === nodeId)
  if (node) {
    selectedNode.value = node
  }
}

const nodes = [
  {
    id: '1',
    label: 'ООП и алгоритмы',
    description: 'Основы ООП, принципы SOLID, базовые алгоритмы сортировки и поиска.',
    video: 'https://www.youtube.com/embed/FI_ME_5U5tc',
    material: 'https://habr.com/ru/articles/148325/',
    assignment: 'Найди примеры 5 алгоритмов сортировки и реализуй один из них.',
    position: {x: 550, y: 50},
    style: {backgroundColor: '#fff', color: '#5656D6', padding: '20px', borderRadius: '10px', fontSize: '36px', fontWeight: 'bold'},
  },
  {
    id: '2',
    label: 'Классы и объекты',
    description: 'Создание и использование классов и объектов на практике.',
    video: 'https://www.youtube.com/embed/6rU_Fgi90R8',
    material: 'https://metanit.com/sharp/tutorial/2.1.php',
    assignment: 'Создай класс "Человек" с полями имя, возраст и методом приветствия.',
    position: {x: 400, y: 200},
    style: {backgroundColor: '#fff', color: '#5656D6', padding: '10px', borderRadius: '10px'},
  },
  {
    id: '3',
    label: 'Наследование',
    description: 'Наследование как способ расширения функциональности классов.',
    video: 'https://www.youtube.com/embed/7WVYqjdMa6U',
    material: 'https://metanit.com/sharp/tutorial/3.1.php',
    assignment: 'Создай класс "Студент", наследующий "Человека", добавь поле "университет".',
    position: {x: 500, y: 300},
    style: {backgroundColor: '#5656D6', color: '#fff', padding: '10px', borderRadius: '10px'},
  },
  {
    id: '4',
    label: 'Полиморфизм',
    description: 'Использование одного интерфейса для разных типов объектов.',
    video: 'https://www.youtube.com/embed/DJ4a7cmjZYI',
    material: 'https://metanit.com/sharp/tutorial/3.2.php',
    assignment: 'Создай базовый класс "Фигура" и реализуй метод "Площадь" в подклассах "Круг" и "Квадрат".',
    position: {x: 300, y: 300},
    style: {backgroundColor: '#5656D6', color: '#fff', padding: '10px', borderRadius: '10px'},
  },
  {
    id: '5',
    label: 'Инкапсуляция',
    description: 'Скрытие деталей реализации и защита данных внутри объекта.',
    video: 'https://www.youtube.com/embed/q6EoRBvdVPQ',
    material: 'https://metanit.com/sharp/tutorial/3.3.php',
    assignment: 'Сделай поля класса "БанкСчёт" приватными и добавь методы для пополнения и снятия.',
    position: {x: 400, y: 400},
    style: {backgroundColor: '#5656D6', color: '#fff', padding: '10px', borderRadius: '10px'},
  },
  {
    id: '6',
    label: 'Абстракция',
    description: 'Выделение существенных характеристик и игнорирование незначительных.',
    video: 'https://www.youtube.com/embed/pTB0EiLXUC8',
    material: 'https://metanit.com/sharp/tutorial/3.4.php',
    assignment: 'Создай абстрактный класс "Транспорт" с методом "Двигаться". Реализуй его в классах "Автомобиль" и "Самолёт".',
    position: {x: 600, y: 500},
    style: {backgroundColor: '#5656D6', color: '#fff', padding: '10px', borderRadius: '10px'},
  },
  {
    id: '7',
    label: 'Рекурсия и итерация',
    description: 'Понимание рекурсии, её применение и сравнение с итерацией.',
    video: 'https://www.youtube.com/embed/ngCos392W4w',
    material: 'https://habr.com/ru/articles/144209/',
    assignment: 'Реализуй факториал числа двумя способами: через рекурсию и через цикл.',
    position: {x: 800, y: 200},
    style: {backgroundColor: '#5656D6', color: '#fff', padding: '10px', borderRadius: '10px'},
  },
  {
    id: '8',
    label: 'Поиск и сортировка',
    description: 'Разбор основных алгоритмов: линейный/бинарный поиск, пузырьковая, быстрая сортировка.',
    video: 'https://www.youtube.com/embed/ZZuD6iUe3Pc',
    material: 'https://habr.com/ru/articles/204600/',
    assignment: 'Реализуй бинарный поиск и пузырьковую сортировку.',
    position: {x: 900, y: 350},
    style: {backgroundColor: '#5656D6', color: '#fff', padding: '10px', borderRadius: '10px'},
  },
]

const edges = [
  {id: 'e1-2', source: '1', target: '2', animated: true},
  {id: 'e2-3', source: '2', target: '3'},
  {id: 'e2-4', source: '2', target: '4'},
  {id: 'e3-5', source: '3', target: '5'},
  {id: 'e5-6', source: '5', target: '6'},
  {id: 'e1-7', source: '1', target: '7'},
  {id: 'e7-8', source: '7', target: '8'},
]
</script>

<style scoped>
.roadmap-flow {
  height: 100vh;
  background: #ffffff;
  font-family: sans-serif;
}

.node-description {
  position: absolute;
  top: 20px;
  right: 20px;
  background: white;
  padding: 16px;
  border-radius: 10px;
  max-width: 400px;
  height: auto;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  overflow-y: auto;
}

.node-description iframe {
  margin-top: 10px;
  margin-bottom: 10px;
  border-radius: 8px;
}

.node-description a {
  display: inline-block;
  margin-top: 10px;
  color: #5656D6;
  font-weight: bold;
  text-decoration: underline;
}

.close-button {
  background: transparent;
  border: none;
  font-size: 20px;
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
  color: #aaa;
  font-weight: bold;
}

.close-button:hover {
  color: #000;
}
</style>

