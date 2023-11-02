def solution():
    # Calculate the minimum grade Carl needs to get on his last test
    total_points_so_far = 80 + 75 + 90  # total points Carl received on the first three tests
    points_needed_on_last_test = 85 * 4 - total_points_so_far  # Carl wants an 85 average for the class and there are four tests total
    result = points_needed_on_last_test
    return result

print(solution())