# 🤖 AI Agent Factory

Uma estrutura modular e extensível para criar, gerenciar e orquestrar agentes de IA autônomos. Este projeto foi desenvolvido para facilitar a construção de ecossistemas de agentes que podem colaborar entre si para resolver tarefas complexas.

## 🚀 Funcionalidades
- **Arquitetura Modular:** Crie novos agentes herdando de uma classe base simples.
- **Definição de Papéis:** Cada agente possui nome, cargo (`role`) e um objetivo específico (`goal`).
- **Memória de Curto Prazo:** Os agentes mantêm um histórico das tarefas executadas durante a sessão.
- **Fácil Integração:** Preparado para conectar com APIs como OpenAI, Anthropic e modelos locais.

## 📁 Estrutura do Projeto
- `core/agent.py`: A alma do projeto. Contém a lógica de definição e execução dos agentes.
- `example.py`: Um guia rápido para você ver seus agentes em ação.
- `requirements.txt`: Lista de dependências para o ambiente Python.

## 🛠️ Como Começar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/bkzoka/ai-agents-factory.git
   cd ai-agents-factory
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure suas chaves:**
   Crie um arquivo `.env` ou exporte sua chave de API:
   ```bash
   export OPENAI_API_KEY='sua-chave-aqui'
   ```

4. **Execute o exemplo:**
   ```bash
   python example.py
   ```

---
Desenvolvido por [bkzoka](https://github.com/bkzoka) ☁️✨
