
# 🐦 Pamps

**Pamps** é uma API que simula uma rede social de microblogs, inspirada no antigo Twitter (X), onde usuários podem criar pequenos posts chamados **pamps**.

O projeto foi desenvolvido com **FastAPI**, utiliza **PostgreSQL** como banco de dados, conta com **autenticação JWT**, está **100% dockerizado** e possui **testes automatizados com Pytest**.

---

## 🚀 Funcionalidades

- ✅ Cadastro e autenticação de usuários (JWT)  
- ✅ Criação, listagem e respostas a posts (pamps)  
- ✅ Relacionamento entre posts como "respostas"  
- ✅ Perfil de usuário com avatar, bio e e-mail  
- ✅ Sistema de refresh token  
- ✅ Banco de dados com PostgreSQL + ORM (SQLModel)  
- ✅ Arquitetura containerizada com Docker  
- ✅ Testes automatizados com Pytest  

---

## 🐳 Tecnologias e Ferramentas

- **Python 3.11+**
- **FastAPI**
- **SQLModel** (baseado em SQLAlchemy + Pydantic)
- **PostgreSQL**
- **Alembic** (controle de migrations)
- **Pytest**
- **Docker & Docker Compose**
- **JWT** (Json Web Tokens para autenticação)
- **Dynaconf** (gerenciamento de configurações)

---

## ⚙️ Como rodar o projeto localmente

### ✅ Pré-requisitos

- Docker  
- Docker Compose  
- Git  

### ▶️ Passos

1️⃣ Clone o repositório:

```bash
git clone https://github.com/diegodutradev/pamps.git
cd pamps
```

2️⃣ Suba os containers:

```bash
docker-compose up --build
```

3️⃣ Aplique as migrations:

```bash
docker-compose exec api alembic upgrade head
```

4️⃣ Acesse a documentação interativa da API:

```
http://localhost:8000/docs
```

---

## 🔑 Autenticação

A autenticação é baseada em **JWT**. Para obter um token, o usuário deve fazer login com `username` e `password`.

Os tokens devem ser enviados no header da requisição:

```
Authorization: Bearer <token>
```

---

## 📁 Estrutura de Pastas

```bash
pamps/
├── models/          # Modelos de dados (User, Post)
├── routes/          # Rotas da API (Auth, User, Post)
├── security/        # Lógica de autenticação e segurança (hash, JWT)
├── db.py            # Configuração do banco de dados
├── config.py        # Configurações com Dynaconf
├── app.py           # Instância principal da FastAPI
├── Dockerfile.dev   # Dockerfile para ambiente de desenvolvimento
├── docker-compose.yml
└── migrations/      # Migrations gerenciadas com Alembic
```

---

## 🧪 Rodando os Testes

```bash
docker-compose exec api pytest
```

Os testes são executados com o banco de dados `pamps_test`.

---

## 📌 Endpoints Principais

| Método | Endpoint          | Descrição                                |
|--------|-------------------|------------------------------------------|
| POST   | /auth/login       | Gera tokens (access e refresh)           |
| POST   | /auth/refresh     | Gera novo token de acesso                |
| POST   | /users/           | Cria novo usuário                        |
| GET    | /users/me         | Retorna dados do usuário autenticado     |
| POST   | /posts/           | Cria um novo pamp                        |
| GET    | /posts/           | Lista todos os pamps                     |
| GET    | /posts/{id}       | Detalhes de um pamp e suas respostas     |

> ⚠️ *A estrutura dos endpoints pode variar conforme a configuração das rotas.*

---

## 📝 Migrations

Criar uma nova migration:

```bash
docker-compose exec api alembic revision --autogenerate -m "Mensagem da migration"
```

Aplicar migrations pendentes:

```bash
docker-compose exec api alembic upgrade head
```

---

## 🔒 Variáveis de Ambiente

As configurações são gerenciadas com **Dynaconf**, através dos arquivos `settings.toml` e `.secrets.toml`.

### Principais variáveis:

| Variável               | Descrição                                |
|------------------------|------------------------------------------|
| PAMPS_DB__uri          | URI do banco PostgreSQL                  |
| PAMPS_DB__connect_args | Configurações adicionais de conexão      |
| SECRET_KEY             | Chave secreta usada no JWT               |
| ALGORITHM              | Algoritmo do JWT (ex: HS256)             |

---

## 🤝 Contribuições

Contribuições são muito bem-vindas!  
Sinta-se à vontade para abrir **issues**, sugerir melhorias ou enviar um **pull request**.

---

## 📄 Licença

Este projeto está licenciado sob os termos da **Licença MIT**.  
Consulte o arquivo `LICENSE` para mais informações.
