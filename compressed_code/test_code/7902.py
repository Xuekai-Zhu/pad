def solution():
    
    total_people = 15
    pizza_eaters_fraction = 3/5
    pizza_eaters = total_people * pizza_eaters_fraction
    pizza_pieces_taken = pizza_eaters * 4
    pizza_pieces_remaining = 50 - pizza_pieces_taken
    result = pizza_pieces_remaining
    return result

print(solution())