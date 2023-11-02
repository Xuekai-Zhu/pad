def solution():
    """Amy biked 12 miles yesterday. If she biked 3 miles less than twice as far as yesterday, how many miles did she bike in total in the two days?"""
    yesterday_miles = 12
    today_miles = (2 * yesterday_miles) - 3
    total_miles = yesterday_miles + today_miles
    result = total_miles
    return result

print(solution())