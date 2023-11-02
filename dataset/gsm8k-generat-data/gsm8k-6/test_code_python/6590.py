def solution():
    # Calculate the total number of hours worked in Weeks 1 and 2
    total_hours_1_2 = 35 * 2

    # Calculate the total number of hours worked in Weeks 3 and 4
    total_hours_3_4 = 48 * 2

    # Calculate the difference in hours worked between Weeks 3-4 and Weeks 1-2
    difference = total_hours_3_4 - total_hours_1_2
    result = difference
    return result

print(solution())