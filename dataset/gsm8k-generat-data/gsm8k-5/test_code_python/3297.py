def solution():
    first_half_distance = 183 * 30  # Tom rides 30 miles per day for the first 183 days
    second_half_days = 365 - 183   # The second half of the year has 365 - 183 = 182 days
    second_half_distance = second_half_days * 35   # Tom rides 35 miles per day for the rest of the 182 days
    total_distance = first_half_distance + second_half_distance  # adding both the distances
    result = total_distance
    return result

print(solution())