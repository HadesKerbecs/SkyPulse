# 🌦️ SkyPulse

Plataforma Full Stack desenvolvida para demonstrar autenticação segura, integração com APIs externas, processamento assíncrono e comunicação entre múltiplos serviços.

O projeto reúne frontend em React, backend em NestJS, autenticação JWT, workers independentes e consumo de APIs públicas, simulando uma arquitetura moderna utilizada em aplicações corporativas.

---

## 🚀 Principais Funcionalidades

### 🔐 Autenticação e Segurança

* Cadastro de usuários
* Login com JWT
* Proteção de rotas
* Sessão autenticada
* Logout automático em caso de expiração do token

### 👥 Gestão de Usuários

* CRUD completo
* Consulta por ID
* Atualização de dados
* Exclusão de registros
* Controle de acesso autenticado

### 🌤️ Integração com APIs Externas

Integração com múltiplos serviços externos:

* Open-Meteo (dados climáticos)
* PokéAPI (informações de Pokémon)
* SWAPI (Star Wars API)

Demonstrando consumo, tratamento e exibição de dados provenientes de diferentes fontes.

### ⚙️ Processamento Assíncrono

O sistema utiliza workers independentes para execução de tarefas paralelas:

* Worker Python para processamento de dados
* Worker Go para tarefas concorrentes
* Comunicação desacoplada entre serviços

### 📊 Dashboard

* Visualização centralizada de informações
* Consumo de APIs em tempo real
* Feedback visual para operações do usuário

---

## 🧠 Desafios Técnicos Resolvidos

Durante o desenvolvimento foram implementadas soluções para:

* Autenticação JWT com expiração automática
* Integração simultânea com múltiplas APIs externas
* Separação de responsabilidades entre frontend e backend
* Processamento assíncrono através de workers
* Containerização completa do ambiente
* Organização modular utilizando NestJS

---

## 🛠️ Tecnologias Utilizadas

### Frontend

* React
* TypeScript
* Vite
* React Router
* Sistema de temas
* Toast Notifications

### Backend

* NestJS
* TypeScript
* JWT Authentication
* Swagger

### Workers

* Python
* Go

### DevOps

* Docker
* Docker Compose
* Git
* GitHub

---

## 🏗️ Arquitetura

```text
Frontend (React)
        │
        ▼
Backend API (NestJS)
        │
 ┌──────┴──────┐
 ▼             ▼
Worker Python  Worker Go
```

A arquitetura foi projetada para demonstrar desacoplamento de responsabilidades, integração entre serviços e processamento paralelo.

---

## 📷 Demonstração

### Tela de Login

*(Inserir screenshot)*

### Dashboard

*(Inserir screenshot)*

### Gestão de Usuários

*(Inserir screenshot)*

### Consulta Climática

*(Inserir screenshot)*

---

## 🔗 APIs Integradas

| API        | Finalidade                  |
| ---------- | --------------------------- |
| PokéAPI    | Consulta de Pokémon         |
| Open-Meteo | Informações climáticas      |
| SWAPI      | Dados do universo Star Wars |

---

## 📚 Endpoints Principais

### Autenticação

| Método | Endpoint       |
| ------ | -------------- |
| POST   | /auth/register |
| POST   | /auth/login    |

### Usuários

| Método | Endpoint   |
| ------ | ---------- |
| GET    | /users     |
| GET    | /users/:id |
| PATCH  | /users/:id |
| DELETE | /users/:id |

Todas as rotas protegidas exigem Bearer Token.

---

## 🐳 Execução com Docker

### Subir ambiente completo

```bash
docker-compose up --build
```

### Serviços Disponíveis

| Serviço     | URL                       |
| ----------- | ------------------------- |
| Frontend    | http://localhost:5173     |
| Backend API | http://localhost:3000     |
| Swagger     | http://localhost:3000/api |

---

## 🎯 Objetivos do Projeto

Este projeto foi desenvolvido para:

* Aplicar conceitos modernos de desenvolvimento Full Stack
* Praticar arquitetura baseada em serviços
* Implementar autenticação segura utilizando JWT
* Trabalhar com integração de APIs externas
* Explorar processamento assíncrono com workers
* Construir uma aplicação de portfólio próxima de cenários corporativos

---

## 📌 Status

✅ Autenticação JWT

✅ CRUD completo de usuários

✅ Integração com APIs externas

✅ Workers independentes

✅ Dockerização completa

✅ Documentação Swagger

✅ Frontend React integrado ao backend NestJS
