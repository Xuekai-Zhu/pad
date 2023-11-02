def solution():
    # Define the total number of gallons needed to fill all the balloons
    total_gallons = 52 * 5

    # Calculate the total time needed to fill the balloons
    time_1 = 10
    time_2 = 5
    time_3 = (total_gallons - (8 * 10 * 52 / 5) - (4 * 5 * 52 / 5)) / (2 * 52)
    total_time = time_1 + time_2 + time_3

    result = total_time
    return result

print(solution())