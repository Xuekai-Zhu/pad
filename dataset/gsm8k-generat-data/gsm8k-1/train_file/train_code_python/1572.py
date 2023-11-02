def solution():
    """Oliver is working out in a gym. On Monday he worked out for 4 hours, and the next day for 2 hours less. On Wednesday he decided to work out twice as much as on Monday. On Thursday the gym was closed, so Oliver needed to exercise at home which took twice as much time as on Tuesday. How many hours in total have Oliver worked out during these four days?"""
    monday_hours = 4
    tuesday_hours = monday_hours - 2
    wednesday_hours = monday_hours * 2
    thursday_hours = tuesday_hours * 2
    total_hours = monday_hours + tuesday_hours + wednesday_hours + thursday_hours
    result = total_hours
    return result

print(solution())