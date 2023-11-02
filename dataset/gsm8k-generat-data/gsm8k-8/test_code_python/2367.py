def solution():
    # Define the number of meals prepared and sold
    lunch_prepared = 17
    lunch_sold = 12

    # Calculate the number of meals remaining
    lunch_remaining = lunch_prepared - lunch_sold

    # Add the remaining lunch meals to the number of dinner meals prepared
    dinner_prepared = lunch_remaining + 5

    result = dinner_prepared
    return result

print(solution())