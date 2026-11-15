import os

import logging

# Configuração de logging para facilitar o debug
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("AIAgent")

class AIAgent:
    def __init__(self, name, role, goal):
        self.name = name
        self.role = role
        self.goal = goal
        self.memory = []

    def execute(self, task):
        if not task:
            logger.error(f"[{self.name}] Nenhuma tarefa fornecida.")
            return "Erro: Tarefa vazia."

        try:
            logger.info(f"[{self.name}] Iniciando tarefa: {task}")
            
            # Simulação de processamento (Aqui seria a integração com OpenAI/Gemini)
            # Em um cenário real, usaríamos: response = openai.ChatCompletion.create(...)
            response = f"Resultado processado por {self.name} ({self.role}): Concluído com sucesso a tarefa '{task}' para atingir o objetivo '{self.goal}'."
            
            self.memory.append({"task": task, "response": response})
            logger.info(f"[{self.name}] Tarefa finalizada.")
            return response
            
        except Exception as e:
            error_msg = f"Erro ao executar tarefa: {str(e)}"
            logger.error(f"[{self.name}] {error_msg}")
            return error_msg

    def get_history(self):
        return self.memory

    def __repr__(self):
        return f"Agent(name={self.name}, role={self.role})"
