def solution():
    """Janina spends $30 each day for rent and uses $12 worth of supplies daily to run her pancake stand. If she sells each pancake for $2, how many pancakes must Janina sell each day to cover her expenses?"""
    # Define the daily expenses
    rent = 30
    supplies = 12

    # Define the selling price per pancake
    selling_price = 2

    # Calculate the total cost per pancake
    total_cost = rent + supplies
    cost_per_pancake = total_cost / selling_price

    # Calculate the number of pancakes Janina must sell to cover her expenses
    pancakes_per_day = round(cost_per_pancake)

    # return the result
    result = pancakes_per_day
    return result

print(solution())