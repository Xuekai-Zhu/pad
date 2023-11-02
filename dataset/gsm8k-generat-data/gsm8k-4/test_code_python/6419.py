def solution():
    """Amber is trying to decide if she wants to spend her $7 on candy or chips. She decides to buy the thing that she can get the most of. The bags of candy cost $1 and contain 12 ounces each. The bags of chips are $1.40 and contain 17 ounces each. How many ounces does she get if she buys the item that gives her the most?"""
    # Define the prices and quantities of candy and chips
    candy_price = 1
    candy_quantity = 12
    chips_price = 1.4
    chips_quantity = 17

    # Calculate the maximum number of ounces Amber can buy with her $7
    max_ounces = 7 / min(candy_price/candy_quantity, chips_price/chips_quantity)

    # Calculate the number of ounces she would get if she buys candy
    candy_ounces = (max_ounces // candy_quantity) * candy_quantity

    # Calculate the number of ounces she would get if she buys chips
    chips_ounces = (max_ounces // chips_quantity) * chips_quantity

    # Choose the item that gives her the most ounces
    if candy_ounces > chips_ounces:
        result = candy_ounces
    else:
        result = chips_ounces
    return result

print(solution())