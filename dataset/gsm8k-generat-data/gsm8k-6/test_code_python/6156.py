def solution():
    # Find the total distance the man drives in 5 hours
    total_distance = 60 * 3 + x * 2  # x is the speed he needs to drive for the next 2 hours

    # Find the average speed required to cover the total distance in 5 hours
    average_speed = total_distance / 5

    # Find the speed he needs to drive for the next 2 hours to get an average speed of 70 mph
    x = (70 * 5 - 60 * 3) / 2
    result = x
    return result

print(solution())