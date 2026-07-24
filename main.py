expenses = []

def greet(name):
    print("Hello",name)

def add_expenses():
    amount = float(input("Enter expenses amount: $"))
    expenses.append(amount)
    print(f"${amount} added successfully!")
def view_expenses():
    for number, expense in enumerate(expenses):
         print("Expense #", number + 1,": $", expense)
def sum_expenses():
    print(f"Total Expenses: ${sum(expenses)}")

def square(number):
    print(number * number)
 
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