def solution():
    school_weeks = 36  # The school year has 36 weeks
    missed_wednesdays = 1  # Jackson missed 1 Wednesday
    missed_fridays = 2  # Jackson missed 2 Fridays
    sandwich_days = (school_weeks * 2) - (missed_wednesdays + missed_fridays)  # Jackson eats sandwiches on Wednesdays and Fridays

    # Calculate the total number of peanut butter and jelly sandwiches eaten
    sandwiches_eaten = sandwich_days * 1  # Jackson eats 1 sandwich per day
    result = sandwiches_eaten
    return result

print(solution())