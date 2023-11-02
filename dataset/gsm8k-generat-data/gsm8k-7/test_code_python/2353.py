def solution():
    num_people = 4
    main_meal_cost = 12.0
    num_appetizers = 2
    appetizer_cost = 6.0
    tip_percent = 0.2
    rush_order_fee = 5.0

    # Calculate the total cost of all main meals
    total_main_meal_cost = num_people * main_meal_cost

    # Calculate the total cost of all appetizers
    total_appetizer_cost = num_appetizers * appetizer_cost

    # Calculate the subtotal (without tip or rush order fee)
    subtotal = total_main_meal_cost + total_appetizer_cost

    # Calculate the amount of tip
    tip_amount = subtotal * tip_percent

    # Add the rush order fee
    total_cost = subtotal + tip_amount + rush_order_fee
    result = total_cost
    return result

print(solution())