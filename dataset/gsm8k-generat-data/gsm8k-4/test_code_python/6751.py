def solution():
    """After buying shirts worth $27 from a store, Dennis received 2 $10 bills and $3 in loose coins for his change. How much money did Dennis have initially?"""
    # Define the cost of the shirts and the amount of change received
    shirts_cost = 27
    change = 2*10 + 3

    # Calculate the initial amount of money Dennis had
    initial_money = shirts_cost + change

    result = initial_money
    return result

print(solution())