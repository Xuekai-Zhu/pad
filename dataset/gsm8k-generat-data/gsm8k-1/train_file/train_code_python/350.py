def solution():
    """Jackson’s mom packs him a peanut butter and jelly sandwich for his school lunch on Wednesdays and Fridays. There are 36 weeks of school and Jackson has only missed 1 Wednesday and 2 Fridays. How many peanut butter and jelly sandwiches did he eat for lunch this school year?"""
    weeks_of_school = 36
    wednesdays_missed = 1
    fridays_missed = 2
    sandwiches_per_week = 2
    total_sandwiches = (weeks_of_school - wednesdays_missed - fridays_missed) * sandwiches_per_week
    result = total_sandwiches
    return result

print(solution())