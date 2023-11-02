def solution():
    # Calculate the number of substitute teachers left after 1 hour
    after_1_hour = 0.5 * 60

    # Calculate the number of substitute teachers left before lunch
    before_lunch = 0.7 * (60 - after_1_hour)

    # Calculate the number of substitute teachers left after lunch
    after_lunch = 60 - after_1_hour - before_lunch
    result = after_lunch
    return result

print(solution())