def solution():
    # Calculate the total number of parking spaces
    total_spaces = 52 + 38

    # Calculate the number of cars parked
    num_cars = 39

    # Calculate the number of spaces filled in the back lot
    back_spaces_filled = 0.5 * 38

    # Calculate the total number of spaces filled
    total_spaces_filled = num_cars + back_spaces_filled

    # Calculate the number of spaces available
    spaces_available = total_spaces - total_spaces_filled
    result = spaces_available
    return result

print(solution())