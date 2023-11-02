def solution():
    total_people = 15
    pizza_eaters = (3/5) * total_people
    pizza_pieces = 50

    # Calculate the total number of pieces of pizza eaten
    total_pieces_eaten = pizza_eaters * 4

    # Calculate the number of pieces of pizza remaining
    remaining_pieces = pizza_pieces - total_pieces_eaten
    result = remaining_pieces
    return result

print(solution())