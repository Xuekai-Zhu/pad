def solution():
    """Anna's mom gave her $10.00 to buy anything she wanted from the candy store.  Anna bought 3 packs of chewing gum for $1.00 each, 5 chocolate bars at $1 each and 2 large candy canes for $0.50 each.  How much money did Anna have left?"""
    # Define the prices of each item
    GUM_PRICE = 1.0
    CHOCOLATE_PRICE = 1.0
    CANDY_CANE_PRICE = 0.5

    # Define the quantities of each item purchased
    gum_quantity = 3
    chocolate_quantity = 5
    candy_cane_quantity = 2

    # Calculate the total cost of each item type
    gum_cost = gum_quantity * GUM_PRICE
    chocolate_cost = chocolate_quantity * CHOCOLATE_PRICE
    candy_cane_cost = candy_cane_quantity * CANDY_CANE_PRICE

    # Calculate the total cost of all items
    total_cost = gum_cost + chocolate_cost + candy_cane_cost

    # Calculate the amount of money left
    money_left = 10.0 - total_cost

    # Display the amount of money left
    result = money_left
    return result

print(solution())