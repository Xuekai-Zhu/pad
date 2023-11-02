def solution():
    """After buying shirts worth $27 from a store, Dennis received 2 $10 bills and $3 in loose coins for his change. How much money did Dennis have initially?"""
    # Calculate the total amount of change received
    change = 2*10 + 3

    # Calculate the initial amount of money Dennis had
    initial_amount = 27 + change

    # Display the initial amount of money
    result = initial_amount
    return result

print(solution())