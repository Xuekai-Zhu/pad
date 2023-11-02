def solution():
    """Chastity bought 4 lollipops which cost $1.50 each, and she also bought 2 packs of gummies which cost $2 each. If she has $15, how much was she left with after spending on the candies?"""
    # Define the prices and quantities of the candies
    lollipop_price = 1.5
    lollipop_quantity = 4
    gummies_price = 2
    gummies_quantity = 2

    # Calculate the total cost of the candies
    total_cost = (lollipop_price * lollipop_quantity) + (gummies_price * gummies_quantity)

    # Calculate the amount left after spending on the candies
    amount_left = 15 - total_cost

    # return the result
    result = amount_left
    return result

print(solution())