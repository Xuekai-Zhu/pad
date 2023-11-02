def solution():
    # Define the number of billboards seen in each hour
    hour1 = 17
    hour2 = 20
    hour3 = 23

    # Calculate the total number of billboards seen
    total_billboards = hour1 + hour2 + hour3

    # Calculate the average number of billboards seen per hour
    average_billboards_per_hour = total_billboards / 3

    result = average_billboards_per_hour
    return result

print(solution())