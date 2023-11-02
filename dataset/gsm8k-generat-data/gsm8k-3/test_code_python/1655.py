def solution():
    """Abe owns a restaurant. Every month he spends a third of his budget on food, a quarter of his budget on restaurant supplies, and the rest of his budget on employee wages. If his budget is $3000 and he uses it up every month, how much is he spending on wages?"""
    # Define Abe's budget
    budget = 3000

    # Calculate the amount spent on food
    food = budget / 3

    # Calculate the amount spent on restaurant supplies
    supplies = budget / 4

    # Calculate the amount spent on wages
    wages = budget - food - supplies

    # Display the amount spent on wages
    result = wages
    return result

print(solution())