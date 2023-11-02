def solution():
    num_flower_plates = 4
    num_checked_plates = 8

    # Calculate the number of polka dotted plates that Jack buys
    num_polka_dotted_plates = 2 * num_checked_plates

    # Calculate the total number of plates before one is smashed
    total_plates = num_flower_plates + num_checked_plates + num_polka_dotted_plates

    # Calculate the number of plates left after one flowered plate is smashed
    plates_left = total_plates - 1
    result = plates_left
    return result

print(solution())