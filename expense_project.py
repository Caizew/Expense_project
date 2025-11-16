expenses = []
income = []
starting = 0
st = 0


def main():
    while True:
        print(
            "enter the order: \n",
            "1.Add expense \n",
            "2.Add income\n",
            "3.See your total expenses\n",
            "4.See your total income\n",
            "5.See your monthly leftover\n",
            "6.Exit\n",
        )
        order = input("enter the number: ")
        if not order.isdigit():
            print("Please enter a valid number! ")
            continue
        if order == "1":
            expense_add()
        elif order == "2":
            income_add()
        elif order == "3":
            show_expenses()
        elif order == "4":
            show_income()
        elif order == "5":
            show_profit_monthly()
        elif order == "6":
            print("You exited the program")
            break
        else:
            print("Invalid choice please try again. \n")


def expense_add():
    name = input("enter the expense name ")
    amount = int(input("enter the amount you had expense: "))
    expenses.append(name)
    expenses.append(amount)


def income_add():
    amount = int(input("enter your new income: "))
    income.append(amount)


def show_expenses():
    global starting
    print(expenses)
    numbers = []
    for i in expenses:
        if type(i) == int:
            numbers.append(i)
    starting = sum(numbers)

    print(starting)


def show_income():
    global st
    st = sum(income)
    print(st)


def show_profit_monthly():
    global st
    global starting
    numbers = []
    for i in expenses:
        if type(i) == int:
            numbers.append(i)
    starting = sum(numbers)
    st = sum(income)
    profit = st - starting
    print(profit)


main()
