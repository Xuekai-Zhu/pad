def solution():
    # Calculate the total cost of the main meals
    main_meals_cost = 4 * 12.0  # Bret and 3 co-workers

    # Calculate the total cost of the appetizers
    appetizers_cost = 2 * 6.0

    # Calculate the total cost of the dinner
    total_cost = main_meals_cost + appetizers_cost

    # Add the 20% tip
    total_cost += 0.2 * total_cost

    # Add the extra $5 rush order fee
    total_cost += 5.0

    result = total_cost
    return result

print(solution())