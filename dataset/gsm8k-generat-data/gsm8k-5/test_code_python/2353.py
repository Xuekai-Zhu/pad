def solution():
    num_people = 4  # Bret and 3 co-workers
    main_meals_cost = 12 * num_people  # Each main meal costs $12
    appetizers_cost = 2 * 6  # Two appetizers that cost $6 each
    subtotal = main_meals_cost + appetizers_cost  # Cost of the food before tip and rush fee

    tip_percent = 0.2  # 20% tip
    tip = subtotal * tip_percent  # Calculate the tip
    rush_fee = 5  # $5 rush fee
    total_cost = subtotal + tip + rush_fee  # Total cost including tip and rush fee
    result = total_cost
    return result

print(solution())