def solution():
    """Chastity bought 4 lollipops which cost $1.50 each, and she also bought 2 packs of gummies which cost $2 each. If she has $15, how much was she left with after spending on the candies?"""
    # Define the cost of each type of candy
    LOLLIPOP_PRICE = 1.5
    GUMMY_PRICE = 2

    # Define the number of each type of candy purchased
    lollipops = 4
    gummies = 2

    # Calculate the total cost of the candies
    candy_cost = lollipops * LOLLIPOP_PRICE + gummies * GUMMY_PRICE

    # Calculate the amount left after spending on the candies
    left = 15 - candy_cost

    # Display the amount left
    result = left
    return result

print(solution())