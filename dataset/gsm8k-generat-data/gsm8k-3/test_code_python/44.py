def solution():
    """James is a first-year student at a University in Chicago. He has a budget of $1000 per semester. He spends 30% of his money on food, 15% on accommodation, 25% on entertainment, and the rest on coursework materials. How much money does he spend on coursework materials?"""
    # Define the total budget
    total_budget = 1000

    # Calculate the amount spent on food
    food_spending = total_budget * 0.3

    # Calculate the amount spent on accommodation
    accommodation_spending = total_budget * 0.15

    # Calculate the amount spent on entertainment
    entertainment_spending = total_budget * 0.25

    # Calculate the remaining budget after all other expenses
    remaining_budget = total_budget - food_spending - accommodation_spending - entertainment_spending

    # Calculate the amount spent on coursework materials
    coursework_spending = remaining_budget

    # Return the result
    result = coursework_spending
    return result

print(solution())