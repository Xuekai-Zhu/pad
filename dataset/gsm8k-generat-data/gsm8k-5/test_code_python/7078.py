def solution():
    # Calculate the number of pieces of bread the first duck ate
    first_duck = 0.5 * (total_pieces_of_bread - 13 - 7 - 30)

    # Calculate the total number of pieces of bread thrown in the pond
    total_pieces_of_bread = 2 * (first_duck + 13 + 7) + 30
    result = total_pieces_of_bread
    return result

print(solution())