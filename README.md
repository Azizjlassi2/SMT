# Gestion de Projet Agile

![Logo](https://github.com/Azizjlassi2/SMT/blob/main/static/Logo.png)

## Description

Ce projet est un API pour un système de gestion de projet agile conçu pour aider les équipes à planifier, suivre et gérer leurs projets de manière efficace. Il offre des fonctionnalités pour gérer des projets, des sprints, des tâches, des rôles d'utilisateurs et des commentaires, facilitant ainsi la collaboration et la transparence au sein des équipes.

## Fonctionnalités

- Création et gestion de projets.
- Organisation des projets en sprints.
- Gestion des tâches avec assignation à des utilisateurs.
- Système de commentaires pour chaque tâche.
- Gestion des rôles d'utilisateur pour définir des permissions.
- Suivi de l'avancement des projets et sprints.

## Technologies Utilisées

- **Django** : Framework web pour le développement du backend.
- **Django REST Framework** : Pour créer une API RESTful.
- **MySQL** : Système de gestion de base de données.
- **Python** : Langage de programmation principal utilisé.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- Python 3.x
- Django
- Django REST Framework
- MySQL

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY` 

`DATABASE_ENGINE` Exemples (PosgreSQL : "django.db.backends.postgresql", MySQL : "django.db.backends.mysql" ...) check [![Django Documentaion](https://docs.djangoproject.com/en/5.1/ref/databases/) for more details.

`DATABASE_NAME`

`DATABASE_USER`

`DATABASE_USER_PASSWORD`

`DATABASE_HOST`

`DATABASE_PORT`

`STATIC_URL` : URL for static files (CSS ,JS ...) Exemples ( "static/")

## Run Locally

Clone the project

```bash
  git clone https://github.com/Azizjlassi2/SMT.git
```

Go to the project directory

```bash
  cd backend
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```

## API Reference

#### Get all projets

```http
  GET api/v1/projets/
```

| Parameter | Type   | Description                                             |
| :-------- | :----- | :------------------------------------------------------ |
| `None`    | `None` | No parameters required. Returns a list of all projects. |

#### Get projet

```http
  GET /api/v1/projets/${id}
```

| Parameter | Type      | Description                               |
| :-------- | :-------- | :---------------------------------------- |
| `id`      | `integer` | **Required**. Id of the project to fetch. |

#### Create a new projet

```http
  POST api/v1/projets/
```

| Parameter     | Type     | Description                                   |
| :------------ | :------- | :-------------------------------------------- |
| `nom`         | `string` | **Required**. Name of the new project.        |
| `description` | `string` | **Optional**. Description of the new project. |

#### Update a projet

```http
  PUT /api/v1/projets/${id}
```

| Parameter     | Type      | Description                                   |
| :------------ | :-------- | :-------------------------------------------- |
| `id`          | `integer` | **Required**. Id of the project to update.    |
| `nom`         | `string`  | **Optional**. Name of the new project.        |
| `description` | `string`  | **Optional**. Description of the new project. |

#### Delete a projet

```http
  DELETE /api/v1/projets/${id}
```

| Parameter | Type      | Description                                |
| :-------- | :-------- | :----------------------------------------- |
| `id`      | `integer` | **Required**. Id of the project to delete. |

#### Get all sprints

```http
  GET api/v1/sprints/
```

| Parameter | Type   | Description                                            |
| :-------- | :----- | :----------------------------------------------------- |
| `None`    | `None` | No parameters required. Returns a list of all sprints. |

#### Get sprint

```http
  GET /api/v1/sprints/${id}
```

| Parameter | Type      | Description                              |
| :-------- | :-------- | :--------------------------------------- |
| `id`      | `integer` | **Required**. Id of the sprint to fetch. |

#### Create a new sprint

```http
  POST api/v1/sprints/
```

| Parameter    | Type      | Description                              |
| :----------- | :-------- | :--------------------------------------- |
| `nom`        | `string`  | **Required**. Name of the new sprint.    |
| `projet`     | `integer` | **Required**. Id of the project to link. |
| `date_debut` | `date`    | **Required**. Start date of the sprint.  |
| `date_fin`   | `date`    | **Required**. End date of the sprint.    |

#### Update a sprint

```http
  PUT /api/v1/sprints/${id}
```

| Parameter    | Type      | Description                                |
| :----------- | :-------- | :----------------------------------------- |
| `id`         | `integer` | **Required**. Id of the project to update. |
| `nom`        | `string`  | **Optional**. Name of the new sprint.      |
| `projet`     | `integer` | **Optional**. Id of the project to link.   |
| `date_debut` | `date`    | **Optional**. Start date of the sprint.    |
| `date_fin`   | `date`    | **Optional**. End date of the sprint.      |

#### Delete a sprint

```http
  DELETE /api/v1/sprints/${id}
```

| Parameter | Type      | Description                               |
| :-------- | :-------- | :---------------------------------------- |
| `id`      | `integer` | **Required**. Id of the sprint to delete. |

#### Get all tasks

```http
  GET api/v1/taches/
```

| Parameter | Type   | Description                                           |
| :-------- | :----- | :---------------------------------------------------- |
| `None`    | `None` | No parameters required. Returns a list of all tasks . |

#### Get task

```http
  GET /api/v1/taches/${id}
```

| Parameter | Type      | Description                            |
| :-------- | :-------- | :------------------------------------- |
| `id`      | `integer` | **Required**. Id of the task to fetch. |

#### Create a new task

```http
  POST api/v1/taches/
```

| Parameter    | Type      | Description                                                                |
| :----------- | :-------- | :------------------------------------------------------------------------- |
| `nom`        | `string`  | **Required**. Name of the new task .                                       |
| `sprint`     | `integer` | **Required**. Id of the sprint to link.                                    |
| `date_debut` | `string`  | **Required**. Status of the task (e.g., "À faire", "En cours", "Terminé"). |

#### Update a task

```http
  PUT /api/v1/taches/${id}
```

| Parameter    | Type      | Description                                                                |
| :----------- | :-------- | :------------------------------------------------------------------------- |
| `id`         | `integer` | **Required**. Id of the task to update.                                    |
| `nom`        | `string`  | **Optional**. Name of the new task .                                       |
| `sprint`     | `integer` | **Optional**. Id of the sprint to link.                                    |
| `date_debut` | `string`  | **Optional**. Status of the task (e.g., "À faire", "En cours", "Terminé"). |

#### Delete a task

```http
  DELETE /api/v1/taches/${id}
```

| Parameter | Type      | Description                             |
| :-------- | :-------- | :-------------------------------------- |
| `id`      | `integer` | **Required**. Id of the task to delete. |

#### Get all commentaires

```http
  GET api/v1/commentaires/
```

| Parameter | Type   | Description                                              |
| :-------- | :----- | :------------------------------------------------------- |
| `None`    | `None` | No parameters required. Returns a list of all comments . |

#### Get task

```http
  GET /api/v1/commentaires/${id}
```

| Parameter | Type      | Description                               |
| :-------- | :-------- | :---------------------------------------- |
| `id`      | `integer` | **Required**. Id of the comment to fetch. |

#### Create a new task

```http
  POST api/v1/commentaires/
```

| Parameter | Type      | Description                               |
| :-------- | :-------- | :---------------------------------------- |
| `contenu` | `string`  | **Required**. Content of the new comment. |
| `tache`   | `integer` | **Required**. Id of the task to link.     |

#### Update a task

```http
  PUT /api/v1/commentaires/${id}
```

| Parameter | Type      | Description                                |
| :-------- | :-------- | :----------------------------------------- |
| `id`      | `integer` | **Required**. Id of the comment to update. |
| `contenu` | `string`  | **Optional**. Content of the new comment.  |

#### Delete a task

```http
  DELETE /api/v1/commentaires/${id}
```

| Parameter | Type      | Description                                |
| :-------- | :-------- | :----------------------------------------- |
| `id`      | `integer` | **Required**. Id of the comment to delete. |

## 🔗 Links

[![linkedin ](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mohamed-aziz-jlassi/)
