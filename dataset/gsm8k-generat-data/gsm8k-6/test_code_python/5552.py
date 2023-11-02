def solution():
    # Calculate the total length of the first three episodes
    length_first_three = 58 + 62 + 65  # minutes

    # Calculate the total length of the four episodes in minutes
    total_length = 4 * 60  # 4 hours

    # Calculate the length of the fourth episode
    length_fourth = total_length - length_first_three  # minutes

    result = length_fourth
    return result

print(solution())