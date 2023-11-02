def solution():
    # Calculate the number of polka dotted plates Jack buys
    num_checked_plates = 8
    num_polka_dotted_plates = 2 * num_checked_plates

    # Calculate the total number of plates Jack has
    total_plates = 4 + 8 + num_polka_dotted_plates

    # Subtract one plate that Jack smashes
    remaining_plates = total_plates - 1

    result = remaining_plates
    return result

print(solution())