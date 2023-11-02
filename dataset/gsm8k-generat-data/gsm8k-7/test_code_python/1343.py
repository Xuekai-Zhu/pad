def solution():
    total_pairs = 1250
    blue_pairs = 540

    # Calculate the number of non-blue pairs
    non_blue_pairs = total_pairs - blue_pairs

    # Divide the non-blue pairs evenly between green and purple
    green_pairs = non_blue_pairs / 2
    purple_pairs = green_pairs

    result = purple_pairs
    return result

print(solution())