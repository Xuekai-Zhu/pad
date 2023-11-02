def solution():
    """Bruce works for 5 hours on Tuesday. On Wednesday he works twice the time he works on Tuesday. On Thursday he works 2 hours less than the time he works on Wednesday. How many hours does Bruce work in all these three days?"""
    tuesday_hours = 5
    wednesday_hours = 2 * tuesday_hours
    thursday_hours = wednesday_hours - 2
    total_hours = tuesday_hours + wednesday_hours + thursday_hours
    result = total_hours
    return result

print(solution())