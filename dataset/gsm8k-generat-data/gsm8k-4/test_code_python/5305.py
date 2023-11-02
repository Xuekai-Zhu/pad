def solution():
    """Natalie bought some food for a party she is organizing. She bought two cheesecakes, an apple pie, and a six-pack of muffins. The six-pack of muffins was two times more expensive than the cheesecake, and one cheesecake was only 25% cheaper than the apple pie. If the apple pie cost $12, how much did Natalie pay for all her shopping?"""
    # Define the price of the apple pie
    apple_pie_price = 12

    # Calculate the price of one cheesecake
    cheesecake_price = apple_pie_price * 1.25 / 2

    # Calculate the price of the six-pack of muffins
    muffins_price = cheesecake_price * 2

    # Calculate the total cost of the food
    total_cost = 2 * cheesecake_price + apple_pie_price + muffins_price

    # Return the result
    result = total_cost
    return result

print(solution())