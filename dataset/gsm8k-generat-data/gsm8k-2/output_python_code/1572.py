def solution():
    """Oliver is working out in a gym. On Monday he worked out for 4 hours, and the next day for 2 hours less. On Wednesday he decided to work out twice as much as on Monday. On Thursday the gym was closed, so Oliver needed to exercise at home which took twice as much time as on Tuesday. How many hours in total have Oliver worked out during these four days?"""
    monday_time = 4
    tuesday_time = monday_time - 2
    wednesday_time = monday_time * 2
    thursday_time = tuesday_time * 2
    total_time = monday_time + tuesday_time + wednesday_time + thursday_time
    result = total_time
    return result

print(solution())