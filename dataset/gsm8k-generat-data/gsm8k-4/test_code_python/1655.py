def solution():
    """Abe owns a restaurant. Every month he spends a third of his budget on food, a quarter of his budget on restaurant supplies, and the rest of his budget on employee wages. If his budget is $3000 and he uses it up every month, how much is he spending on wages?"""
    # Define the restaurant's budget
    budget = 3000

    # Calculate the amount spent on food
    food_spending = budget * (1/3)

    # Calculate the amount spent on restaurant supplies
    supplies_spending = budget * (1/4)

    # Calculate the amount spent on wages
    wages_spending = budget - food_spending - supplies_spending

    # Return the result
    result = wages_spending
    return result

print(solution())