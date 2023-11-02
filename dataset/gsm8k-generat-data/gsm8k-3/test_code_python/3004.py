def solution():
    """Bill is trying to decide whether to make blueberry muffins or raspberry muffins. Blueberries cost $5.00 per 6 ounce carton and raspberries cost $3.00 per 8 ounce carton. If Bill is going to make 4 batches of muffins, and each batch takes 12 ounces of fruit, how much money would he save by using raspberries instead of blueberries?"""
    # Define the cost and amount of fruit needed for each batch of muffins
    BLUEBERRY_COST = 5.00 / 6
    BLUEBERRY_AMOUNT = 12 / 6
    RASPBERRY_COST = 3.00 / 8
    RASPBERRY_AMOUNT = 12 / 8

    # Calculate the total cost of using blueberries
    blueberry_total_cost = BLUEBERRY_COST * BLUEBERRY_AMOUNT * 4

    # Calculate the total cost of using raspberries
    raspberry_total_cost = RASPBERRY_COST * RASPBERRY_AMOUNT * 4

    # Calculate the amount saved by using raspberries instead of blueberries
    savings = blueberry_total_cost - raspberry_total_cost

    # Display the amount saved
    result = savings
    return result

print(solution())