import json
from datetime import datetime

# Arquivo onde as tarefas serão salvas
FILENAME = 'tasks.json'

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, description, due_date, priority):
        """Adiciona uma nova tarefa."""
        task = {
            'description': description,
            'due_date': due_date,
            'priority': priority,
            'completed': False
        }
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self, completed=False):
        """Lista tarefas pendentes ou concluídas."""
        tasks = [t for t in self.tasks if t['completed'] == completed]
        for task in tasks:
            status = 'Concluída' if task['completed'] else 'Pendente'
            print(f"Descrição: {task['description']}, Prazo: {task['due_date']}, Prioridade: {task['priority']}, Status: {status}")

    def mark_task_completed(self, description):
        """Marca uma tarefa como concluída."""
        for task in self.tasks:
            if task['description'] == description:
                task['completed'] = True
                self.save_tasks()
                return True
        return False

    def remove_task(self, description):
        """Remove uma tarefa."""
        self.tasks = [t for t in self.tasks if t['description'] != description]
        self.save_tasks()

    def filter_tasks_by_priority(self, priority):
        """Filtra tarefas por prioridade."""
        tasks = [t for t in self.tasks if t['priority'] == priority and not t['completed']]
        for task in tasks:
            print(f"Descrição: {task['description']}, Prazo: {task['due_date']}, Prioridade: {task['priority']}")

    def save_tasks(self):
        """Salva as tarefas em um arquivo JSON."""
        with open(FILENAME, 'w') as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        """Carrega as tarefas do arquivo JSON."""
        try:
            with open(FILENAME, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

# Interface simples para o usuário
def main():
    manager = TaskManager()

    while True:
        print("\nSistema de Gerenciamento de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas Pendentes")
        print("3. Listar Tarefas Concluídas")
        print("4. Marcar Tarefa como Concluída")
        print("5. Remover Tarefa")
        print("6. Filtrar Tarefas por Prioridade")
        print("0. Sair")

        option = input("Escolha uma opção: ")

        if option == '1':
            description = input("Descrição da tarefa: ")
            due_date = input("Prazo (YYYY-MM-DD): ")
            priority = input("Prioridade (alta, média, baixa): ")
            manager.add_task(description, due_date, priority)

        elif option == '2':
            manager.list_tasks(completed=False)

        elif option == '3':
            manager.list_tasks(completed=True)

        elif option == '4':
            description = input("Descrição da tarefa a marcar como concluída: ")
            if manager.mark_task_completed(description):
                print("Tarefa marcada como concluída.")
            else:
                print("Tarefa não encontrada.")

        elif option == '5':
            description = input("Descrição da tarefa a remover: ")
            manager.remove_task(description)
            print("Tarefa removida.")

        elif option == '6':
            priority = input("Filtrar por prioridade (alta, média, baixa): ")
            manager.filter_tasks_by_priority(priority)

        elif option == '0':
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
