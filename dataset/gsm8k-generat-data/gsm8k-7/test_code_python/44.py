def solution():
    budget = 1000
    food_percentage = 0.3
    accommodation_percentage = 0.15
    entertainment_percentage = 0.25

    # Calculate the total percentage of money spent on food, accommodation, and entertainment
    total_percentage_spent = food_percentage + accommodation_percentage + entertainment_percentage

    # Calculate the total amount spent on food, accommodation, and entertainment
    total_spent = total_percentage_spent * budget

    # Calculate the amount spent on coursework materials
    coursework_materials_spent = budget - total_spent
    result = coursework_materials_spent
    return result

print(solution())