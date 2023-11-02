def solution():
    # Calculate the total number of tulips needed for the smiley face
    num_red_tulips = 8 * 2 + 18  # 8 for each eye and 18 for the smile
    num_yellow_tulips = 9 * 18  # 9 times the number of tulips in the smile
    total_tulips = num_red_tulips + num_yellow_tulips  # total number of tulips needed
    result = total_tulips
    return result

print(solution())