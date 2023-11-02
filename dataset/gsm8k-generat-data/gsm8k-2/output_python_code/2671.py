def solution():
    """In a house of 15, 3/5 of the people eat pizza. If Aviana brought pizza with 50 pieces, and each person eating pizza took 4 pieces, calculate the number of pizza pieces that remained."""
    total_people = 15
    pizza_eaters = int(total_people * (3/5))
    pizza_pieces = 50
    pieces_per_person = 4
    total_pieces_eaten = pizza_eaters * pieces_per_person
    pieces_remaining = pizza_pieces - total_pieces_eaten
    result = pieces_remaining
    return result

print(solution())