def solution():
    # Define the number of chocolates Delphine ate each day
    day1 = 4
    day2 = 2 * day1 - 3
    day3 = day1 - 2
    day4 = day3 - 1

    # Calculate the total number of chocolates Delphine ate
    total_eaten = day1 + day2 + day3 + day4

    # Calculate the number of chocolates remaining
    remaining = 24 - total_eaten
    result = remaining
    return result

print(solution())