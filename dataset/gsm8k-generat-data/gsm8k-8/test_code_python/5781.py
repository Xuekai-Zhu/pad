def solution():
    # Define the cost of each item
    white_bread_cost = 3.5
    baguette_cost = 1.5
    sourdough_bread_cost = 4.5
    croissant_cost = 2

    # Define the quantity of each item needed per week
    white_bread_quantity = 2
    baguette_quantity = 1
    sourdough_bread_quantity = 2
    croissant_quantity = 1

    # Calculate the total cost per week
    total_cost_per_week = (white_bread_cost * white_bread_quantity) + (baguette_cost * baguette_quantity) + (sourdough_bread_cost * sourdough_bread_quantity) + (croissant_cost * croissant_quantity)

    # Calculate the total cost over 4 weeks
    total_cost_over_4_weeks = total_cost_per_week * 4
    result = total_cost_over_4_weeks
    return result

print(solution())