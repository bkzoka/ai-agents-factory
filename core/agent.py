import os

class AIAgent:
    def __init__(self, name, role, goal):
        self.name = name
        self.role = role
        self.goal = goal
        self.memory = []

    def execute(self, task):
        print(f"[{self.name}] Executando: {task}")
        # Aqui entraria a chamada para uma LLM
        response = f"Resultado simulado para: {task}"
        self.memory.append({"task": task, "response": response})
        return response

    def __repr__(self):
        return f"Agent(name={self.name}, role={self.role})"
