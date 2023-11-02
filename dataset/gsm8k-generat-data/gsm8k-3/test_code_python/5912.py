def solution():
    """A school canteen sells a sandwich at $2, a hamburger at $2, one stick of hotdog at $1, and a can of fruit juice at $2 each can. Selene buys three sandwiches and a can of fruit juice. Tanya buys two hamburgers and two cans of fruit juice.  How much do Selene and Tanya spend together?"""
    # Define the prices of the different items
    SANDWICH_PRICE = 2
    HAMBURGER_PRICE = 2
    HOTDOG_PRICE = 1
    JUICE_PRICE = 2

    # Selene's order
    selene_sandwiches = 3
    selene_juice = 1
    selene_total = (selene_sandwiches * SANDWICH_PRICE) + (selene_juice * JUICE_PRICE)

    # Tanya's order
    tanya_hamburgers = 2
    tanya_juice = 2
    tanya_total = (tanya_hamburgers * HAMBURGER_PRICE) + (tanya_juice * JUICE_PRICE)

    # Total cost
    total_cost = selene_total + tanya_total

    # Display the total cost
    result = total_cost
    return result

print(solution())