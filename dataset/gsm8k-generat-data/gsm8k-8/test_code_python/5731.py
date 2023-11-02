def solution():
    # Define the original balance and the amount spent on groceries and gas
    balance = 126.00
    spent_on_groceries = 60.00
    spent_on_gas = spent_on_groceries / 2

    # Calculate the new balance after the grocery and gas purchases
    new_balance = balance + spent_on_groceries + spent_on_gas

    # Subtract the amount from the returned towels
    new_balance -= 45.00

    result = new_balance
    return result

print(solution())