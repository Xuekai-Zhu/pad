def solution():
    # Count of billboards seen in each hour
    billboards_hour1 = 17
    billboards_hour2 = 20
    billboards_hour3 = 23

    # Total count of billboards seen
    total_billboards = billboards_hour1 + billboards_hour2 + billboards_hour3

    # Average count of billboards per hour
    average_billboards = total_billboards / 3

    result = average_billboards
    return result

print(solution())