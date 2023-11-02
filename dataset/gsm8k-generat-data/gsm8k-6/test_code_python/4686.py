def solution():
    # Calculate the total number of clothing items
    total_clothes = 20 + 8  # 20 shirts and 8 pairs of shorts
    # Calculate the number of clothes that are already folded
    folded_clothes = 12 + 5  # 12 shirts and 5 pairs of shorts are already folded
    # Calculate the remaining clothes to fold
    remaining_clothes = total_clothes - folded_clothes
    result = remaining_clothes
    return result

print(solution())