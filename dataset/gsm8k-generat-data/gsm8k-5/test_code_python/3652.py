def solution():
    # Calculate the cost of adult meals
    adult_meals_cost = 6 * 6  # 6 adults, each meal costs $6

    # Calculate the cost of children's meals
    children_meals_cost = 2 * 4  # 2 children, each meal costs $4

    # Calculate the cost of drinks
    drinks_cost = 8 * 2  # 6 adults and 2 children, each ordered a soda for $2

    # Calculate the total bill
    total_bill = adult_meals_cost + children_meals_cost + drinks_cost
    result = total_bill
    return result

print(solution())