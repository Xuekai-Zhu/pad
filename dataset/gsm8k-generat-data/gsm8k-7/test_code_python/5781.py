def solution():
    white_bread_cost = 3.5
    num_white_bread_loaves = 2

    baguette_cost = 1.5

    sourdough_bread_cost = 4.5
    num_sourdough_bread_loaves = 2

    almond_croissant_cost = 2.0

    weeks = 4

    # Calculate the total cost of all white bread loaves
    total_white_bread_cost = white_bread_cost * num_white_bread_loaves

    # Calculate the total cost of all sourdough bread loaves
    total_sourdough_bread_cost = sourdough_bread_cost * num_sourdough_bread_loaves

    # Calculate the total cost of all items Candice buys per visit
    total_visit_cost = total_white_bread_cost + baguette_cost + total_sourdough_bread_cost + almond_croissant_cost

    # Calculate the total amount Candice spends over 4 weeks
    total_spent = total_visit_cost * weeks
    result = total_spent
    return result

print(solution())