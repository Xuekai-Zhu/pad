def solution():
    num_chocolates = 24

    # Calculate the number of chocolates eaten on each day
    day1 = 4
    day2 = 2 * day1 - 3
    day3 = day1 - 2
    day4 = day2 - 1
    total_eaten = day1 + day2 + day3 + day4

    # Calculate the number of uneaten chocolates
    uneaten_chocolates = num_chocolates - total_eaten
    result = uneaten_chocolates
    return result

print(solution())