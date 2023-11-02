def solution():
    """Josie received $50 as a gift. She plans to buy two cassette tapes that cost $9 each and a headphone set that costs $25. How much money will she have left?"""
    # Define the initial amount of money
    initial_money = 50

    # Define the cost of the cassette tapes and the headphone set
    cassette_tape_cost = 9
    headphone_cost = 25

    # Calculate the total cost of the items
    total_cost = 2 * cassette_tape_cost + headphone_cost

    # Calculate the amount of money left
    money_left = initial_money - total_cost

    # return the result
    result = money_left
    return result

print(solution())