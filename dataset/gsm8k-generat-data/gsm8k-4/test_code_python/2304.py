def solution():
    """Amy's grandfather gave her $100 for her birthday. Amy bought 3 dolls, each of which cost $1. How much money does Amy have left?"""
    # Define the initial amount of money
    initial_money = 100

    # Define the cost of each doll and the number of dolls purchased
    doll_cost = 1
    num_dolls = 3

    # Calculate the total cost of the dolls
    total_cost = doll_cost * num_dolls

    # Calculate the amount of money left after purchasing the dolls
    money_left = initial_money - total_cost

    # Return the result
    result = money_left
    return result

print(solution())