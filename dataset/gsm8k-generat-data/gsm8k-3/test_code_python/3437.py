def solution():
    """John receives $100 from his uncle and gives his sister Jenna 1/4 of that money. He goes and buys groceries worth $40. How much money does John have remaining?"""
    # John's initial amount of money
    initial_money = 100

    # Amount of money given to Jenna
    jenna_money = initial_money * (1/4)

    # Amount of money spent on groceries
    grocery_cost = 40

    # Amount of money remaining
    remaining_money = initial_money - jenna_money - grocery_cost

    # Display the amount of money remaining
    result = remaining_money
    return result

print(solution())