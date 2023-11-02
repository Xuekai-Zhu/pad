def solution():
    """A school canteen sells a sandwich at $2, a hamburger at $2, one stick of hotdog at $1, and a can of fruit juice at $2 each can. Selene buys three sandwiches and a can of fruit juice. Tanya buys two hamburgers and two cans of fruit juice. How much do Selene and Tanya spend together?"""
    # Define the prices of each item
    SANDWICH_PRICE = 2
    HAMBURGER_PRICE = 2
    HOTDOG_PRICE = 1
    FRUIT_JUICE_PRICE = 2

    # Calculate the total cost for Selene
    selene_cost = (3 * SANDWICH_PRICE) + FRUIT_JUICE_PRICE

    # Calculate the total cost for Tanya
    tanya_cost = (2 * HAMBURGER_PRICE) + (2 * FRUIT_JUICE_PRICE)

    # Calculate the total cost for both Selene and Tanya
    total_cost = selene_cost + tanya_cost

    # return the result
    result = total_cost
    return result

print(solution())