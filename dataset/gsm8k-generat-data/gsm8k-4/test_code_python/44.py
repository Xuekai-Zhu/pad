def solution():
    """James is a first-year student at a University in Chicago. He has a budget of $1000 per semester. He spends 30% of his money on food, 15% on accommodation, 25% on entertainment, and the rest on coursework materials. 
    How much money does he spend on coursework materials?"""
    
    # Define the budget and the percentages spent on different categories
    budget = 1000
    food_percentage = 0.3
    accommodation_percentage = 0.15
    entertainment_percentage = 0.25
    
    # Calculate the total amount spent on food and accommodation
    food_spending = budget * food_percentage
    accommodation_spending = budget * accommodation_percentage
    
    # Calculate the total amount spent on entertainment
    entertainment_spending = budget * entertainment_percentage
    
    # Calculate the total amount spent on coursework materials
    coursework_spending = budget - food_spending - accommodation_spending - entertainment_spending
    
    # Return the result
    result = coursework_spending
    return result

print(solution())