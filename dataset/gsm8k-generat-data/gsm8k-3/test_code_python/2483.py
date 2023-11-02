def solution():
    """Josie received $50 as a gift. She plans to buy two cassette tapes that cost $9 each and a headphone set that costs $25. How much money will she have left?"""
    # Define the cost of each item
    TAPE_PRICE = 9
    HEADPHONE_PRICE = 25

    # Define the number of each item purchased
    tape_count = 2

    # Calculate the total cost of the tapes
    tape_cost = TAPE_PRICE * tape_count

    # Calculate the total cost of all the items
    total_cost = tape_cost + HEADPHONE_PRICE

    # Calculate the amount of money left
    money_left = 50 - total_cost

    # Display the money left
    result = money_left
    return result

print(solution())