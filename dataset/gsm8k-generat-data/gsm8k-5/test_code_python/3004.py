def solution():
    blueberry_price = 5.00  # Blueberries cost $5.00 per 6 ounce carton
    raspberry_price = 3.00  # Raspberries cost $3.00 per 8 ounce carton
    ounces_per_batch = 12  # Each batch takes 12 ounces of fruit
    batches = 4  # Bill is making 4 batches of muffins

    # Calculate the cost of using blueberries
    blueberry_cost = (batches * ounces_per_batch / 6) * blueberry_price

    # Calculate the cost of using raspberries
    raspberry_cost = (batches * ounces_per_batch / 8) * raspberry_price

    # Calculate the amount saved by using raspberries instead of blueberries
    savings = blueberry_cost - raspberry_cost
    result = savings
    return result

print(solution())