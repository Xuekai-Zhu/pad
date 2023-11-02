def solution():
    """Mom went shopping at the market. She left with €55. She bought 2 packs of bananas for €4 each, pears for €2, asparagus for €6 and finally a chicken for €11. How much money does Mom have left?"""
    # Define the prices of each item
    BANANA_PRICE = 4
    PEAR_PRICE = 2
    ASPARAGUS_PRICE = 6
    CHICKEN_PRICE = 11

    # Define the quantity of each item purchased
    banana_quantity = 2
    pear_quantity = 1
    asparagus_quantity = 1
    chicken_quantity = 1

    # Calculate the total cost of the items purchased
    total_cost = (banana_quantity * BANANA_PRICE) + (pear_quantity * PEAR_PRICE) + (asparagus_quantity * ASPARAGUS_PRICE) + (chicken_quantity * CHICKEN_PRICE)

    # Calculate the amount of money Mom has left
    remaining_money = 55 - total_cost

    # Display the amount of money Mom has left
    result = remaining_money
    return result

print(solution())