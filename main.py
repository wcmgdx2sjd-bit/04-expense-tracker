expenses = []


while True:
    print("Expense Tracker")

    print("1. Add expense") 

    print("2. View expenses")

    print("3. Total expenses")

    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You chose add expense")
        amount = float(input("Enter expenses amount: $"))
        expenses.append(amount)
        print(f"${amount} added successfully!")

    elif choice == "2":
        print("You chose view expenses") 
          
        for number, expense in enumerate(expenses):
            print("Expense #", number + 1,": $", expense)
            
    elif choice == "3":
        print(sum(expenses))

    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")