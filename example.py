from core.agent import AIAgent
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente de um arquivo .env se existir
load_dotenv()

def main():
    # Verifica se existe uma API Key configurada (apenas exemplo)
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Aviso: Variável de ambiente 'OPENAI_API_KEY' não encontrada. Usando modo simulação.")

    # Criando um agente pesquisador
    researcher = AIAgent(
        name="Cl0udly-Helper",
        role="Pesquisador de Tecnologia",
        goal="Encontrar as últimas tendências em IA"
    )

    print(f"\n--- Agente Criado: {researcher} ---")
    
    # Teste de execução normal
    result = researcher.execute("Quais são as novidades sobre o Gemini 3?")
    print(f"\nResposta do Agente:\n{result}\n")

    # Teste de erro (tarefa vazia)
    error_test = researcher.execute("")
    print(f"Teste de Erro: {error_test}")

if __name__ == "__main__":
    main()
