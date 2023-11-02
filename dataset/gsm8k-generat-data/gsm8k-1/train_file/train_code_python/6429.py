def solution():
    """On the weekend, Tony will walk to the store. On weekdays, he runs to the store. When he walks, he goes 2 MPH. When he runs he goes 10 MPH. The store is 4 miles away. If he goes on Sunday, Tuesday, and Thursday, what is the average time in minutes that he spends to get to the store?"""
    weekend_time = 4 / 2 * 60 # distance / speed * 60 to convert to minutes
    weekday_time = 4 / 10 * 60
    total_time = weekend_time*2 + weekday_time*3 # Tony goes on Sunday, Tuesday, and Thursday
    average_time = total_time / 3
    result = average_time
    return result

print(solution())