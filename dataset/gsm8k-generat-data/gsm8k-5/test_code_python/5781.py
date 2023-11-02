def solution():
    white_bread_cost = 3.5  # Cost of one loaf of white bread
    baguette_cost = 1.5  # Cost of one baguette
    sourdough_bread_cost = 4.5  # Cost of one loaf of sourdough bread
    croissant_cost = 2.0  # Cost of one almond croissant
    weeks = 4  # Candice is buying bread for 4 weeks

    # Calculate the total cost of white bread for 4 weeks
    white_bread_total_cost = 2 * white_bread_cost * weeks

    # Calculate the total cost of sourdough bread for 4 weeks
    sourdough_bread_total_cost = 2 * sourdough_bread_cost * weeks

    # Calculate the total cost of baguettes for 4 weeks
    baguette_total_cost = baguette_cost * weeks

    # Calculate the total cost of croissants for 4 weeks
    croissant_total_cost = croissant_cost * weeks

    # Calculate the total cost of all bread and croissants for 4 weeks
    total_cost = white_bread_total_cost + sourdough_bread_total_cost + baguette_total_cost + croissant_total_cost

    result = total_cost
    return result

print(solution())