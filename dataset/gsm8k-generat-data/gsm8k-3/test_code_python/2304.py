def solution():
    """Amy's grandfather gave her $100 for her birthday. Amy bought 3 dolls, each of which cost $1. How much money does Amy have left?"""
    # Define the initial amount of money Amy received
    INITIAL_AMOUNT = 100

    # Define the cost of each doll
    DOLL_PRICE = 1

    # Calculate the total cost of the dolls
    dolls_cost = DOLL_PRICE * 3

    # Calculate the amount of money Amy has left
    money_left = INITIAL_AMOUNT - dolls_cost

    # Display the amount of money left
    result = money_left
    return result

print(solution())