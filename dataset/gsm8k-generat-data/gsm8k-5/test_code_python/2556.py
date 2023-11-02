def solution():
    white_rhino_weight = 5100  # One white rhino weighs 5100 pounds
    black_rhino_weight = 2000  # One black rhino weighs 1 ton, or 2000 pounds
    num_white_rhinos = 7  # There are 7 white rhinos
    num_black_rhinos = 8  # There are 8 black rhinos

    # Calculate the total weight of the white rhinos
    total_white_rhino_weight = white_rhino_weight * num_white_rhinos

    # Calculate the total weight of the black rhinos
    total_black_rhino_weight = black_rhino_weight * num_black_rhinos

    # Calculate the total weight of all the rhinos
    total_weight = total_white_rhino_weight + total_black_rhino_weight
    result = total_weight
    return result

print(solution())