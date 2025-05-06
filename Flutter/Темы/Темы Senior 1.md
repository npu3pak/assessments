1. CI/CD
- Понятие Continuous Integration
- Понятие Continuous Delivery
- GitLab CI. Термины: runner, pipeline, stage, job, artifact
- GitLab CI. Настройка сборки в .gitlab-ci.yaml
- GitLab CI. Настройка CI/CD Variables
- GitLab CI. Подключение новой машины в качестве runner
- Fastlane. Возможности. Настройка
- Firebase App Distribution. Возможности. Настройка. Подключение тестировщиков.

2. HTTPS
- Краткое описание
- TLS Handshake
- Атака Man-in-the-middle
- SSL Pinning. Реализация в Dart
- Перехват SSL трафика на мобильных устройствах с помощью HTTP Toolkit

3. RX
- Описание концепции
- Observables
- Single
- Subject
- Schedulers
- Операции: map, filter, merge, zip, subscribe, flatmap, scan, distinct

4. WebRTC
- Краткое описание технологии
- Проект LiveKit и библиотека livekit_client

5. Подготовка сборок к публикации
- Требования к публикации для iOS
- Требования к публикации для Android
- Подписание приложений iOS
- Подписание приложений Android

6. Публикация в Google Play, Huawei AppGallery, RuStore, AppStore
- Публикация новой версии приложения
- Время рассмотрения сборок
- Возможности отложенной публикации
- Возможности бета-тестирования
- Формат AppBundle и его преобразование в APK
- Дополнительные возможности кроме публикации

7. Кастомизация сборок Flutter с помощью Flavors
- Настройка проекта Android/iOS
- Определение типа сборки
- Передача информации о типе сборки во Flutter-модуль
- Сборка с указанием Flavor

8. Публикация плагинов pub.dev
- Как подготовить плагин к публикации
- Как опубликовать плагин

9. Кодогенерация
- Пакет freezed
- Пакет json_serializable
- Пакет mason
- OpenAPI Generator
- Dart Macros

10. Расчет покрытия модульными тестами
- Что такое code coverage
- Как рассчитать покрытие тестами для проекта
- Как сгенерировать отчет о покрытии тестами

11. Основы Python
- Особенности синтаксиса
- Условные операторы
- Циклы
- Функции
- Списки, множества, словари
- Подключение модулей и работа с pip
- Вывод текста
- Чтение и запись файлов
- Обработка исключений
- Запуск команд bash из python-скриптов

12. Основы Bash
- Что такое bash. Аналоги. Hashbang
- Получение помощи. man
- Навигация по файловой системе.
- Запись результатов выполнения команд в файл. stdout, stderr
- Создание каталогов и файлов
- Просмотр каталогов и файлов. cat, tail
- Разрешения. chmod
- Суперпользователь. sudo
- Фильтрация вывода. grep
- Поиск и остановка запущенных процессов. ps, kill
- Команда echo
- Условный оператор
- Цикл for
- Функции

13. Flutter. Внутреннее устройство
- Архтектура Flutter. Framework. Engine. Embedder
- 3 Trees Architecture. Widgets. Elements. Render objects. BuildContext
- Bindings. SchedulerBinding. GestureBinding. RendererBinding. WidgetsBinding. ServicesBinging
- Асинхронность. Event Loop. MicroTask. Event
- Внутренняя реализация анимаций. Ticker и TickerProvider
- Sound Null Safety. Иерархия классов для nullable и не nullable типов

14. Flutter. Isolates
- Отличия изолятов от потоков
- Запуск изолятов. Isolate.run(), Isolate.spawn(), compute
- Обмен сообщениями между изолятами

15. Flutter. Работа в фоновом режиме
- Headless execution
- Директива @pragma(vm:entry-point)
- Запуск dart-кода из приложения, запущенного в фоновом режиме. CallbackHandle
- Плагин workmanager

16. Flutter. Фрагментные шейдеры
- Что такое фрагментные шейдеры и как они работают?
- Загрузка и использование шейдеров во Flutter-приложении
- Передача параметров из Flutter-виджета в шейдер
- Как сделать фрагментный шейдер, рисующий круг, который плавно меняет свой цвет в течение времени?

17. Flutter. Профилирование и оптимизация
- Профилирование. Возможности инструментария Flutter
- Профилирование. Запуск в режиме профилирования
- Профилирование. Performance Overlay и Performance VIew. UI thread. Raster thread. Jank
- Профилирование. CPU Profiler View. Поиск медленных участков кода.
- Профилирование. Memory View. Определение утечек памяти. Причины утечек памяти
- Профилирование. Инструменты анализа размера приложения
- Оптимизация. Shader compilation jank. Причины и решение проблемы
- Оптимизация. Определение областей перерисовки экрана. Виджет RepaintBoundary
- Оптимизация. Impeller. Преимущества и недостатки. Включение и отключение
- Оптимизация. Performance best practices

18. Flutter. Распространенные фреймворки и архитектуры
- Riverpod
- Provider
- GetX
- Redux