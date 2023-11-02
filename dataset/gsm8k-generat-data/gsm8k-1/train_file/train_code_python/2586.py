def solution():
    """In order to train for his fights Rocky would run 4 miles on day one of training. Rocky would double the miles for day 2, and triple the miles from day 2 for day 3. How many miles did Rocky run in the first three days of training?"""
    day1_miles = 4
    day2_miles = day1_miles * 2
    day3_miles = day2_miles * 3
    total_miles = day1_miles + day2_miles + day3_miles
    result = total_miles
    return result

print(solution())