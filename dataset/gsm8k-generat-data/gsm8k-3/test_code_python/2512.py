def solution():
    """Scott wants to make and freeze a large batch of ratatouille.  At the farmers' market he buys 5 pounds of eggplants and 4 pounds of zucchini at $2.00 a pound.  He needs 4 pounds of tomatoes that are $3.50 a pound.  The onions are $1.00 a pound and he needs 3 pounds.  Then he needs a pound of basil which is sold for $2.50 per half pound.  If this yields 4 quarts, how much does each quart cost?"""
    # Define the prices and quantities of ingredients
    EGGPLANT_PRICE = 2.00
    ZUCCHINI_PRICE = 2.00
    TOMATO_PRICE = 3.50
    ONION_PRICE = 1.00
    BASIL_PRICE = 2.50 / 0.5  # price per pound

    EGGPLANT_QTY = 5
    ZUCCHINI_QTY = 4
    TOMATO_QTY = 4
    ONION_QTY = 3
    BASIL_QTY = 1

    # Calculate the total cost of each ingredient
    eggplant_cost = EGGPLANT_QTY * EGGPLANT_PRICE
    zucchini_cost = ZUCCHINI_QTY * ZUCCHINI_PRICE
    tomato_cost = TOMATO_QTY * TOMATO_PRICE
    onion_cost = ONION_QTY * ONION_PRICE
    basil_cost = BASIL_QTY * BASIL_PRICE

    # Calculate the total cost of all the ingredients
    total_cost = eggplant_cost + zucchini_cost + tomato_cost + onion_cost + basil_cost

    # Calculate the cost per quart
    cost_per_quart = total_cost / 4

    # Display the cost per quart
    result = cost_per_quart
    return result

print(solution())