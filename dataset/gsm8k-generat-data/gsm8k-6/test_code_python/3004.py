def solution():
    # Calculate the cost of using blueberries for 4 batches of muffins
    blueberry_cost = (5/6) * 4 * 12 * 4  # $5.00 per 6 ounce carton, 4 batches, 12 ounces per batch, 4 hours of baking
    # Calculate the cost of using raspberries for 4 batches of muffins
    raspberry_cost = (3/8) * 4 * 12 * 4  # $3.00 per 8 ounce carton, 4 batches, 12 ounces per batch, 4 hours of baking
    # Calculate the amount saved by using raspberries instead of blueberries
    amount_saved = blueberry_cost - raspberry_cost
    result = amount_saved
    return result

print(solution())