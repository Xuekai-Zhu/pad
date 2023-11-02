def solution():
    num_hotdogs = 5
    hotdog_price = 1.5

    num_salads = 3
    salad_price = 2.5

    money_given = 20

    # Calculate the total cost of all hotdogs
    total_hotdog_cost = num_hotdogs * hotdog_price

    # Calculate the total cost of all salads
    total_salad_cost = num_salads * salad_price

    # Calculate the total cost of the meal
    total_cost = total_hotdog_cost + total_salad_cost

    # Calculate the change
    change = money_given - total_cost
    result = change
    return result

print(solution())