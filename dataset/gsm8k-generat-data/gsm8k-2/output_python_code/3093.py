def solution():
    """Gina can paint six cups an hour with roses and 7 cups an hour with lilies. Her Etsy store gets an order for 6 rose cups and 14 lily cups. If Gina gets paid $90 total for the order, how much does she make per hour?"""
    rose_time = 6 / 6
    lily_time = 14 / 7
    total_time = rose_time + lily_time
    hourly_pay = 90 / total_time
    result = hourly_pay
    return result

print(solution())