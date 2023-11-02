def solution():
    # Calculate the total cost of coloring books and peanuts
    coloring_books_cost = 2 * 4
    peanuts_cost = 4 * 1.5
    total_cost = coloring_books_cost + peanuts_cost

    # Calculate the cost of the stuffed animal
    stuffed_animal_cost = 25 - total_cost
    result = stuffed_animal_cost
    return result

print(solution())