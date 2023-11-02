def solution():
    # Calculate the number of chocolates Delphine ate on each day
    day1 = 4
    day2 = 2 * day1 - 3
    day3 = day1 - 2
    day4 = day2 - 1
    total_eaten = day1 + day2 + day3 + day4

    # Calculate the number of chocolates remaining after 5 days
    remaining = 24 - total_eaten
    result = remaining
    return result

print(solution())