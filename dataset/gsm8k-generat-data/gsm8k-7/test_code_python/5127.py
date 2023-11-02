def solution():
    curtis_meal_cost = 16.0
    rob_meal_cost = 18.0
    discount_percent = 0.5  # 50% discount
    total_meal_cost = curtis_meal_cost + rob_meal_cost

    # Calculate the total cost of the meal after the discount is applied
    discounted_meal_cost = total_meal_cost * (1 - discount_percent)

    result = discounted_meal_cost
    return result

print(solution())