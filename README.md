# rag_agent 🤖📄

Este projeto consiste em um **Agente Inteligente com arquitetura RAG** (Retrieval-Augmented Generation), projetado para processar documentos, tomar decisões autônomas e oferecer suporte técnico qualificado.

A solução utiliza tecnologias de ponta para garantir escalabilidade, persistência de dados e uma interface amigável.

---

## 🚀 Funcionalidades

* **Arquitetura RAG**: Recuperação de informações em documentos locais para respostas contextuais e precisas.
* **Tomada de Decisão**: Agente capaz de utilizar ferramentas para decidir a melhor ação com base no input do usuário.
* **Persistência de Dados**: Integração com banco de vetores ChromaDB para armazenamento permanente de embeddings.
* **Interface Web**: Visualização interativa e amigável desenvolvida com Streamlit.
* **Ambiente Dockerizado**: Configuração completa com Docker e Docker Compose para deploy simplificado e reprodutível.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem**: [Python 3.13](https://www.python.org/)
* **Orquestração de IA**: [LangChain](https://www.langchain.com/) & [LangChain-Google-Genai](https://pypi.org/project/langchain-google-genai/)
* **Modelo de Linguagem (LLM)**: Google Gemini API
* **Banco de Dados de Vetores**: [ChromaDB](https://www.trychroma.com/)
* **Interface**: [Streamlit](https://streamlit.io/)
* **Gestão de Dependências**: [Poetry](https://python-poetry.org/)
* **Infraestrutura**: [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)

---

## 📂 Estrutura do Projeto

```text
rag_agent/
├── rag_agent/              # Lógica central do pacote Python
│   ├── agents/             # Definição das personalidades e lógica dos agentes
│   ├── core/               # Recursos compartilhados (prompts, tools, settings)
│   └── rag/                # Lógica de processamento de documentos e vetores
├── view/                   # Interface de usuário (Streamlit)
├── knowledge/              # Documentos brutos (PDFs/TXTs) para a base do RAG
├── tests/                  # Testes automatizados com Pytest
├── Dockerfile              # Configuração da imagem Docker
└── docker-compose.yml      # Orquestração de containers e volumes
```

---

## ⚙️ Como Executar

### Pré-requisitos

* Possuir o **Docker** e **Docker Compose** instalados.
* Uma chave de API do **Google Gemini**.

### Passo a Passo

1. **Clone o repositório**:

    ```bash
    git clone [https://github.com/rogeriocampos07/rag_agent.git](https://github.com/rogeriocampos07/rag_agent.git)
    cd rag_agent
    ```

2. **Configure as variáveis de ambiente**:
    Crie um arquivo `.env` na raiz do projeto seguindo o modelo:

    ```bash
    GOOGLE_API_KEY=sua_chave_aqui
    CHROMA_DB_PATH=/app/chroma_db
    ```

3. **Suba o container**:

    ```bash
    docker compose up --build
    ```

4. **Acesse a interface**:

    O agente estará disponível em `http://localhost:8501`.

---

## 🧪 Testes e Qualidade

O projeto utiliza **Ruff** para linting e **Pytest** para testes automatizados. Você pode rodar as tarefas de qualidade diretamente pelo container:

```bash
# Rodar todos os testes
docker exec -it rag_agent_container poetry run task test

# Formatar e verificar estilo do código
docker exec -it rag_agent_container poetry run task format
```

---

## 👤 Autor

Desenvolvido por **Rogério Campos**.

-**Docker Hub**: [rogeriocampos07](https://hub.docker.com/u/rogeriocampos07)

---

> **Nota**: Para garantir que a integração siga as diretrizes de performance e boas práticas para ferramentas Google, este projeto consulta a documentação oficial da ADK em [https://google.github.io/adk-docs/](https://google.github.io/adk-docs/).
