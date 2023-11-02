def solution():
    # Convert Monday's distance to meters
    monday_distance = 9 * 1000

    # Calculate the total distance for Wednesday and Friday
    wed_fri_distance = 4816 + 2095

    # Calculate how many meters farther Hannah ran on Monday than Wednesday and Friday
    diff_distance = monday_distance - wed_fri_distance

    result = diff_distance
    return result

print(solution())