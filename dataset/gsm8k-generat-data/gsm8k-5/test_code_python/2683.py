def solution():
    # Calculate the total number of magazines Alexandra bought
    total_magazines = 8 + 12 + (4 * 8)  # On Friday she bought 8, Saturday 12 more, Sunday 4 times as many as Friday

    # Subtract the number of magazines the dog chewed up
    remaining_magazines = total_magazines - 4

    result = remaining_magazines
    return result

print(solution())