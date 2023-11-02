def solution():
    """On the weekend, Tony will walk to the store. On weekdays, he runs to the store. When he walks, he goes 2 MPH. When he runs he goes 10 MPH. The store is 4 miles away. If he goes on Sunday, Tuesday, and Thursday, what is the average time in minutes that he spends to get to the store?"""
    distance = 4
    walk_speed = 2
    run_speed = 10
    sunday_time = distance / walk_speed
    tuesday_time = distance / run_speed
    thursday_time = distance / run_speed
    total_time = sunday_time + tuesday_time + thursday_time
    average_time = total_time / 3 * 60
    result = average_time
    return result

print(solution())