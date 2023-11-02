def solution():
    """Amanda received $50 as a gift. She plans to buy two cassette tapes that cost $9 each and a headphone set that costs $25. How much money will she have left?"""
    # Define the cost of each cassette tape and the headphone set
    TAPE_COST = 9
    HEADPHONE_COST = 25

    # Define the amount of money Amanda received as a gift
    gift_money = 50

    # Calculate the total cost of the cassette tapes
    tape_cost = TAPE_COST * 2

    # Calculate the total cost of all the items Amanda plans to buy
    total_cost = tape_cost + HEADPHONE_COST

    # Calculate the amount of money Amanda will have left after buying the items
    left_money = gift_money - total_cost

    # Display the amount of money Amanda will have left
    result = left_money
    return result

print(solution())