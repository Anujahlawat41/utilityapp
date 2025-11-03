import requests

# ======================
# 🔢 CALCULATOR MODULE
# ======================
def calculator():
    print("\n===== 🧮 CALCULATOR =====")
    print("Operations: +  -  *  /")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operator!")
            return

        print(f"Result: {result}\n")
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.\n")


# ======================
# 📝 TO-DO LIST MODULE
# ======================
tasks = []

def todo_app():
    while True:
        print("\n===== 📝 TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter new task: ")
            tasks.append(task)
            print("✅ Task added!")
        elif choice == '2':
            if not tasks:
                print("No tasks available.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
        elif choice == '3':
            if not tasks:
                print("No tasks to delete.")
            else:
                num = int(input("Enter task number to delete: "))
                if 0 < num <= len(tasks):
                    deleted = tasks.pop(num - 1)
                    print(f"🗑️ Deleted task: '{deleted}'")
                else:
                    print("Invalid task number.")
        elif choice == '4':
            break
        else:
            print("Invalid choice, try again.")


# ======================
# 💱 CURRENCY CONVERTER MODULE
# ======================
def currency_converter():
    print("\n===== 💱 CURRENCY CONVERTER =====")
    from_curr = input("From currency (e.g., USD): ").upper()
    to_curr = input("To currency (e.g., INR): ").upper()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    try:
        url = f"https://api.exchangerate.host/convert?from={from_curr}&to={to_curr}&amount={amount}"
        response = requests.get(url)
        data = response.json()
        if data.get("result"):
            print(f"{amount} {from_curr} = {round(data['result'], 2)} {to_curr}\n")
        else:
            print("⚠️ Could not fetch conversion rate.")
    except Exception as e:
        print("❌ Error fetching data:", e)


# ======================
# 🏠 MAIN MENU
# ======================
def main():
    while True:
        print("\n===============================")
        print("  🔧 PYTHON UTILITY APP")
        print("===============================")
        print("1. 🧮 Calculator")
        print("2. 📝 To-Do List")
        print("3. 💱 Currency Converter")
        print("4. 🚪 Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            calculator()
        elif choice == '2':
            todo_app()
        elif choice == '3':
            currency_converter()
        elif choice == '4':
            print("Goodbye 👋")
            break
        else:
            print("Invalid option! Please choose again.\n")

# Run the App
if __name__ == "__main__":
    main()
