def solution():
    """Janina spends $30 each day for rent and uses $12 worth of supplies daily to run her pancake stand. If she sells each pancake for $2, how many pancakes must Janina sell each day to cover her expenses?"""
    # Define the daily rent and supply costs
    DAILY_RENT = 30
    DAILY_SUPPLIES = 12

    # Define the price at which each pancake is sold
    PANCAKE_PRICE = 2

    # Calculate the total cost per day
    total_cost = DAILY_RENT + DAILY_SUPPLIES

    # Calculate the number of pancakes Janina must sell to cover her expenses
    pancakes_needed = total_cost / PANCAKE_PRICE

    # Round up to the nearest integer because Janina cannot sell a fraction of a pancake
    pancakes_needed = math.ceil(pancakes_needed)

    # Display the number of pancakes Janina must sell
    result = pancakes_needed
    return result

print(solution())