from core.agent import AIAgent

def main():
    # Criando um agente pesquisador
    researcher = AIAgent(
        name="Cl0udly-Helper",
        role="Pesquisador de Tecnologia",
        goal="Encontrar as últimas tendências em IA"
    )

    print(f"Agente Criado: {researcher}")
    
    result = researcher.execute("Quais são as novidades sobre o Gemini 3?")
    print(f"Resposta do Agente: {result}")

if __name__ == "__main__":
    main()
