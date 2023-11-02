def solution():
    # Define James' budget and the percentages he spends on different categories
    budget = 1000
    food_percent = 0.3
    accommodation_percent = 0.15
    entertainment_percent = 0.25

    # Calculate the amount of money James spends on food, accommodation, and entertainment
    food_spending = budget * food_percent
    accommodation_spending = budget * accommodation_percent
    entertainment_spending = budget * entertainment_percent

    # Calculate the total amount of money James spends on these categories
    total_spending = food_spending + accommodation_spending + entertainment_spending

    # Calculate how much money James has left for coursework materials
    coursework_materials_spending = budget - total_spending

    result = coursework_materials_spending
    return result

print(solution())