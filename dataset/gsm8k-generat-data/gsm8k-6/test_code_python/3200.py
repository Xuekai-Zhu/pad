def solution():
    # Calculate the total length of ribbon used
    length_used = 100 * 0.15  # each piece is 0.15 meters long
    # Calculate the length of ribbon remaining
    length_remaining = 51 - length_used  # 51 meters is the initial length of ribbon
    result = length_remaining
    return result

print(solution())