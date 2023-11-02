def solution():
    """Amanda received $50 as a gift. She plans to buy two cassette tapes that cost $9 each and a headphone set that costs $25. How much money will she have left?"""
    # Define the total amount of money Amanda received
    total_money = 50

    # Define the cost of the cassette tapes and the headphone set
    cassette_tape_cost = 9
    headphone_cost = 25

    # Calculate the total cost of the items Amanda wants to buy
    total_cost = 2 * cassette_tape_cost + headphone_cost

    # Calculate the amount of money Amanda will have left
    money_left = total_money - total_cost

    result = money_left
    return result

print(solution())