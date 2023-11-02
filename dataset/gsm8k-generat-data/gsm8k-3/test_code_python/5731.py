def solution():
    """Marian's pending credit card balance is $126.00.  She puts $60.00 worth of groceries on her card and half that amount in gas.  She returned some bath towels for $45.00.  What's the new balance on her credit card?"""
    # Define the initial credit card balance and the cost of groceries and gas
    initial_balance = 126.00
    groceries = 60.00
    gas = 30.00

    # Subtract the cost of the groceries and gas from the initial balance
    balance = initial_balance - groceries - gas

    # Add the amount from returning the bath towels
    balance += 45.00

    # Display the new balance
    result = balance
    return result

print(solution())