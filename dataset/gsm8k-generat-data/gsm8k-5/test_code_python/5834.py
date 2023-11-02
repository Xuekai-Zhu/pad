def solution():
    # Calculate the total number of spaces in both parking lots
    total_spaces = 52 + 38

    # Calculate the number of spaces filled in the back parking lot
    filled_spaces = 38 / 2

    # Calculate the total number of filled spaces
    total_filled = 39 + filled_spaces

    # Calculate the number of available spaces
    available_spaces = total_spaces - total_filled
    result = available_spaces
    return result

print(solution())