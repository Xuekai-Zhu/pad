def solution():
    """Scott wants to buy a skateboard. To make money, Scott sold berry smoothies for $3 a cup and cakes for $2 each. He sold 40 cups of smoothies and 18 cakes. How much money did he make?"""
    # Define the price of a smoothie and a cake
    SMOOTHIE_PRICE = 3
    CAKE_PRICE = 2

    # Define the number of smoothies and cakes sold
    smoothies_sold = 40
    cakes_sold = 18

    # Calculate the total amount of money made
    total_money = (smoothies_sold * SMOOTHIE_PRICE) + (cakes_sold * CAKE_PRICE)

    # Display the total amount of money made
    result = total_money
    return result

print(solution())