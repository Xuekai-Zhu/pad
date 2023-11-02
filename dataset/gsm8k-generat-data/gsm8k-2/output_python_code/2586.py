def solution():
    """In order to train for his fights Rocky would run 4 miles on day one of training. Rocky would double the miles for day 2, and triple the miles from day 2 for day 3. How many miles did Rocky run in the first three days of training?"""
    day_one_miles = 4
    day_two_miles = 2 * day_one_miles
    day_three_miles = 3 * day_two_miles
    total_miles = day_one_miles + day_two_miles + day_three_miles
    result = total_miles
    return result

print(solution())