def solution():
    """In a house of 15, 3/5 of the people eat pizza. If Aviana brought pizza with 50 pieces, and each person eating pizza took 4 pieces, calculate the number of pizza pieces that remained."""
    total_people = 15
    pizza_eaters_fraction = 3/5
    pizza_eaters = total_people * pizza_eaters_fraction
    pizza_pieces_taken = pizza_eaters * 4
    pizza_pieces_remaining = 50 - pizza_pieces_taken
    result = pizza_pieces_remaining
    return result

print(solution())