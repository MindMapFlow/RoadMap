import { defineStore } from 'pinia'
import axios from 'axios'

export const useRoadmapStore = defineStore('roadmap', {
    state: () => ({
        roadmap: { topics: [], dependencies: [], materials: [] },
        loading: false,
        error: null
    }),
    actions: {
        async fetchRoadmap(syllabusId) {
            this.loading = true
            this.error = null
            try {
                const response = await axios.get(`http://localhost:8000/api/syllabus/${syllabusId}/`)
                this.roadmap = response.data
            } catch (error) {
                this.error = 'Ошибка загрузки роадмапа'
                console.error('Ошибка загрузки роадмапа:', error)
            } finally {
                this.loading = false
            }
        },
        async generateRoadmap(syllabusId) {
            this.loading = true
            this.error = null
            try {
                const response = await axios.post(`http://localhost:8000/api/syllabus/${syllabusId}/generate-roadmap/`)
                this.roadmap = response.data.roadmap
            } catch (error) {
                this.error = 'Ошибка генерации роадмапа'
                console.error('Ошибка генерации роадмапа:', error)
            } finally {
                this.loading = false
            }
        },
        // Мок-генерация для тестирования без бэкенда
        mockGenerateRoadmap() {
            this.loading = true
            this.error = null
            setTimeout(() => {
                this.roadmap = {
                    topics: [
                        {
                            title: "Культура мышления: исторический экскурс",
                            description: "Изучение основ философского мышления.",
                            order: 1,
                            subtopics: [
                                {
                                    title: "Философия как тип знания",
                                    description: "Анализ философии как особого типа знания.",
                                    order: 1,
                                    subtopics: []
                                },
                                {
                                    title: "Историческое развитие философии",
                                    description: "Обзор эволюции философской мысли.",
                                    order: 2,
                                    subtopics: []
                                }
                            ]
                        },
                        {
                            title: "Теоретические основы философии: диалог души и тела",
                            description: "Исследование онтологии и гносеологии.",
                            order: 2,
                            subtopics: [
                                {
                                    title: "Бытие",
                                    description: "Основы бытия в философии.",
                                    order: 1,
                                    subtopics: []
                                }
                            ]
                        }
                    ],
                    dependencies: [
                        {
                            from: "Культура мышления: исторический экскурс",
                            to: "Теоретические основы философии: диалог души и тела"
                        }
                    ],
                    materials: [
                        {
                            topic: "Философия как тип знания",
                            type: "assignment",
                            title: "Эссе (200 слов)",
                            url: "",
                            content: "Эссе (200 слов)"
                        },
                        {
                            topic: "Историческое развитие философии",
                            type: "video",
                            title: "Видео: История философии",
                            url: "https://youtube.com/philosophy_history",
                            content: "Обзор эволюции философской мысли."
                        }
                    ]
                }
                this.loading = false
            }, 1000)
        }
    },
    getters: {
        getTopics: (state) => state.roadmap.topics || [],
        getDependencies: (state) => state.roadmap.dependencies || [],
        getMaterials: (state) => (topicTitle) =>
            state.roadmap.materials?.filter(material => material.topic === topicTitle) || []
    }
})