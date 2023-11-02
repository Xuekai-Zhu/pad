def solution():
    """Amy biked 12 miles yesterday. If she biked 3 miles less than twice as far as yesterday, how many miles did she bike in total in the two days?"""
    yesterday_distance = 12
    today_distance = 2 * yesterday_distance - 3
    total_distance = yesterday_distance + today_distance
    result = total_distance
    return result

print(solution())