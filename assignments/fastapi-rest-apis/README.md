# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Aprender a criar APIs REST utilizando o framework FastAPI, explorando conceitos como rotas, métodos HTTP, validação de dados e documentação automática.

## 📝 Tasks

### 🛠️ Criar uma API REST básica

#### Description

Implemente uma API REST que gerencie um recurso simples (ex: tarefas, usuários ou produtos). A API deve incluir operações básicas de CRUD (Create, Read, Update, Delete).

#### Requirements
Completed program should:

- Criar rotas para cada operação CRUD
- Validar dados de entrada utilizando Pydantic
- Retornar respostas apropriadas com códigos HTTP
- Incluir documentação automática gerada pelo FastAPI

#### Example

Exemplo de endpoints:

- `POST /items/` - Criar um novo item
- `GET /items/{id}` - Obter detalhes de um item
- `PUT /items/{id}` - Atualizar um item existente
- `DELETE /items/{id}` - Remover um item

Opcionalmente, forneça um arquivo `starter-code.py` com uma estrutura inicial para os alunos começarem.