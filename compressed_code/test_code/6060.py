def solution():
    
    coloring_book_cost = 4 * 2
    peanuts_cost = 1.5 * 4
    total_cost = coloring_book_cost + peanuts_cost
    stuffed_animal_cost = 25 - total_cost
    result = stuffed_animal_cost
    return result

print(solution())