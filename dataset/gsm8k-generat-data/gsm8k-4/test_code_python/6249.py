def solution():
    """Raul had $87 to spare so he decided to go to the bookshop. Raul bought 8 comics, each of which cost $4. How much money does Raul have left?"""
    # Define the price of each comic and the initial amount of money Raul had
    COMIC_PRICE = 4
    INITIAL_MONEY = 87

    # Calculate the total cost of the comics Raul bought
    total_cost = COMIC_PRICE * 8

    # Calculate the amount of money Raul has left
    money_left = INITIAL_MONEY - total_cost

    # Return the result
    result = money_left
    return result

print(solution())