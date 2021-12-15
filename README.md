Project "Resume Site"
===========
___
This project was built with Django. To conveniently fill out forms, django-admin is used, with which you can edit information on the project pages. This includes editing the homepage. Development projects pages. Enabling and disabling links to github. As well as editing data for communication.

Home page
-----------
___
For convenience, you can use different CVs written in advance. To select which one to use, use the select button in django-admin. Uploading a photo for a resume is also supported.

Projects page
-----------
___
This page is used to display your projects on github with their descriptions. Adding also via django-admin. Includes the creation of categories of projects, phases of the development phase, a description of the project itself and a photo if desired.

Data page
-----------
___
Page with data for feedback. Also, the data is filled in by choice and implemented through django-admin.
___
Other
-----------
___
The sqlite database is used to save the data. The choice fell on this base because of the simple design of the project itself. Use .env to keep your private database and private key. There are special fields in .env for using postgresql. For sqllite in .env, only use the private key field. 



Проект "Сайт-резюме"
======
____
Данный проект создан с помощью Django. Для удобного заполнения форм используется django-admin, с помощью которого вможете редактировать
информации на страничках проекта. Это включает в себя редактирование главной страницы. Страницы с разрабытываемыми проектами. Включение и отключение ссылок на гитхаб. А так же редактирование данный для связи.

Главная страница
-----------
____
Для удобства вы можете использовать разные резюме написаные заранее. Для выбора какое именно использовать используется кнопка-выбор в django-admin.
Так же поддерживается загрузка фото для резюме.

Страница с проектами
-----------
___
Эта страница используется для отображение ваших проектов на гитхаб с их описанием.
Добавление так же через django-admin. Включает в себя создание категорий проектов, фазы этапа разработки, описание самого проекта и фото по желанию.


Страница с данными
-----------
___
Страница с данными для обратной связи. Так же данные заполняются по выбору и реализуются через django-admin.
___
Прочее
-----------
Для сохранения данных используеться БД sqlite. Выбор пал на эту базу данный из-за несложной конструкции самого проекта.
Для сохранения личных о БД и секретного ключа исполюзуйте .env. Для использование postgresql в .env есть специальные поля. Для sqllite в .env используйте только поле секретного ключа.