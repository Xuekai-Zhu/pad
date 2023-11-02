def solution():
    # Calculate the number of spaces already occupied by planted vegetables
    occupied_spaces = (3 * 5) + (5 * 4) + 30  # 3 kinds of tomatoes with 5 each, 5 kinds of cucumbers with 4 each, and 30 potatoes

    # Calculate the total number of spaces in the garden
    total_spaces = 10 * 15  # 10 rows with 15 spaces each

    # Calculate the number of empty spaces remaining in the garden
    empty_spaces = total_spaces - occupied_spaces
    result = empty_spaces
    return result

print(solution())