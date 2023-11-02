def solution():
    # Calculate the cost of blueberries per ounce
    blueberry_cost = 5/6

    # Calculate the cost of raspberries per ounce
    raspberry_cost = 3/8

    # Calculate the cost savings per ounce by using raspberries
    savings_per_ounce = blueberry_cost - raspberry_cost

    # Calculate the total amount of fruit needed for 4 batches of muffins
    total_fruit_needed = 4 * 12

    # Calculate the total cost savings by using raspberries instead of blueberries
    total_savings = savings_per_ounce * total_fruit_needed

    return total_savings

print(solution())