def solution():
    side_length = 16 
    bush_length = 4 
    num_sides = 3

    # Calculate the total length of all sides that need bushes
    total_length = side_length * num_sides

    # Calculate the number of bushes needed to cover the total length
    num_bushes = total_length / bush_length
    result = num_bushes
    return result

print(solution())