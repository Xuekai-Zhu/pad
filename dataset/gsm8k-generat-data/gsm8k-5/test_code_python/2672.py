def solution():
    # Calculate the total number of people who eat pizza in the house
    pizza_eaters = 3/5 * 15

    # Calculate the total number of pizza pieces consumed
    pieces_consumed = pizza_eaters * 4

    # Calculate the number of pizza pieces left
    pieces_left = 50 - pieces_consumed
    result = pieces_left
    return result

print(solution())