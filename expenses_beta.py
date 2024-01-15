import csv
import os
from datetime import datetime

#editar categorias
class ExpenseTracker:
    ALLOWED_CATEGORIES = ["compras", "escola", "coisas"]

    def __init__(self):
        self.expenses = {}

        # Cria um arquivo CSV se não existir
        self.file_path = "expenses.csv"
        if not self.file_exists():
            self.create_csv_file()

    def file_exists(self):
        return os.path.exists(self.file_path)

    def create_csv_file(self):
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount (€)", "Description"])

    def add_expense(self, category, amount, description):
        if category.lower() not in self.ALLOWED_CATEGORIES:
            print("Categoria inválida. Escolha entre:", self.ALLOWED_CATEGORIES)
            return

        date_today = datetime.now().strftime("%d-%m-%Y")
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date_today, category.lower(), f"{amount:.2f} €", description])

        print(f"Despesa de {amount:.2f} € adicionada à categoria {category} em {date_today}.")

    def view_expenses(self, month=None):
        print("Despesas:")
        with open(self.file_path, mode='r') as file:
            reader = csv.DictReader(file)

            # Verifica se o arquivo está vazio (senão cria)
            if not reader.fieldnames:
                print("Nenhuma despesa registada.")
                return

            for row in reader:
                if month is None or (month and row['Date'].split('-')[1] + '-' + row['Date'].split('-')[2] == month):
                    # Adiciona verificação para evitar KeyError
                    amount = row.get('Amount', 'N/A')
                    description = row.get('Description', 'N/A')
                    print(f"{row['Date']} - {row['Category']}: {amount} ({description})")


# Exemplo de uso
tracker = ExpenseTracker()

while True:
    print("\n1. Adicionar despesa")
    print("2. Visualizar despesas por mês")
    print("3. Sair")

    choice = input("Escolha uma opção (1/2/3): ")

    if choice == '1':
        category = input("Digite a categoria da sua despesa (compras/escola/coisas): ")
        amount = float(input("Digite o valor da despesa em euros: "))
        description = input("Digite uma descrição para a despesa: ")
        tracker.add_expense(category, amount, description)
    elif choice == '2':
        month = input("Digite o mês para visualizar as despesas (formato MM-YYYY): ")
        tracker.view_expenses(month)
    elif choice == '3':
        print("A sair...")
        break
    else:
        print("Opção inválida. Tente novamente.")