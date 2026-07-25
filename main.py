expenses = []
    
try:
     with open("expenses.txt","r") as file:
      contents = file.read()

     expenses = contents.splitlines() 
        
     for number, expense in enumerate(expenses):

      expenses[number] = float(expense)
except FileNotFoundError:
    print("No expenses file found yet")      

def add_expenses():
    try:
         amount = float(input("Enter expenses amount: $"))

         expenses.append(amount)

         with open("expenses.txt", "a") as file:
                file.write(str(amount) + "\n")

         print(f"${amount:.2f} added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_expenses():
    for number, expense in enumerate(expenses):
         print(f"Expense #{number + 1}: ${expense:.2f}")

def sum_expenses():
    print(f"Total Expenses: ${sum(expenses):.2f}")

while True:
    print("Expense Tracker")
    print("1. Add expense") 
    print("2. View expenses")
    print("3. Total expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expenses()  
          
    elif choice == "2":
        view_expenses()
            
    elif choice == "3":
        sum_expenses()

    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")