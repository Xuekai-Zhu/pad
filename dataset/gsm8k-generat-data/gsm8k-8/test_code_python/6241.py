def solution():
    # Calculate the total number of pieces
    total_pieces = 5 * 8

    # Calculate the number of pieces per person
    pieces_per_person = total_pieces / 4

    # Calculate the number of calories per person
    calories_per_person = 80 * pieces_per_person
    result = calories_per_person
    return result

print(solution())