def solution():
    # Calculate the total cost of the coloring books
    coloring_books_cost = 2 * 4

    # Calculate the total cost of the peanuts
    peanuts_cost = 4 * 1.5

    # Calculate the total cost of the items before the stuffed animal
    total_cost_before_stuffed_animal = coloring_books_cost + peanuts_cost

    # Calculate the cost of the stuffed animal
    stuffed_animal_cost = 25 - total_cost_before_stuffed_animal

    result = stuffed_animal_cost
    return result

print(solution())