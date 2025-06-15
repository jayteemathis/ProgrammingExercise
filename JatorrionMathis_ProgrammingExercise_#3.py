#this program allows the user to input their monthly expenses,
#uses reduce() to calculate the total, highest, and lowest expenses,
#displays a summary of the results.

from functools import reduce

#function to collect expense inputs from the user
def get_expenses():
    #make an empty list to store the expenses
    expenses = []

    #tell the user for input
    print("Enter your monthly expenses. Type 'done' when finished.\n")

    #until the user types 'done'
    while True:
        expense_type = input("Enter the type of expense (or 'done' to finish): ")

        #break the loop if user is finished
        if expense_type.lower() == 'done':
            break

        #prompt for the amount and handle invalid input
        try:
            amount = float(input(f"Enter the amount for {expense_type}: "))
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")
            continue

        #add the (type, amount) pair to the list
        expenses.append((expense_type, amount))

    # the list of expenses
    return expenses

# calculate the total of all expenses
def calculate_total(expenses):
    # reduce to sum the second item (amount) from each tuple
    return reduce(lambda acc, item: acc + item[1], expenses, 0)

#function to find the highest expense
def find_highest(expenses):
    #reduce to find the tuple with the highest amount
    return reduce(lambda a, b: a if a[1] > b[1] else b, expenses)

#function to find the lowest expense
def find_lowest(expenses):
    #reduce to find the tuple with the lowest amount
    return reduce(lambda a, b: a if a[1] < b[1] else b, expenses)

# display the summary of results
def display_summary(total, highest, lowest):
    #print the total, highest, and lowest expenses
    print("\nExpense Summary:")
    print(f"Total Expense: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")

#main function that drives the program
def main():
    #get the list of expenses from the user
    expenses = get_expenses()

    #no expenses were entered, show a message and stop
    if not expenses:
        print("No expenses entered. Exiting program.")
        return

    #calculate the total, highest, and lowest expenses
    total = calculate_total(expenses)
    highest = find_highest(expenses)
    lowest = find_lowest(expenses)

    #display the results
    display_summary(total, highest, lowest)

# Run the program
if __name__ == "__main__":
    main()