def solution():
    """Tabitha agreed to pay John and Jill $10 an hour to help clean out her attic and basement. Jill worked 2 hours on Saturday and 1 hour on Sunday. John worked twice as long as Jill on Saturday and three times as long as Jill on Sunday. How much more money did John earn compared to Jill?"""
    hourly_rate = 10
    jill_saturday_hours = 2
    jill_sunday_hours = 1
    john_saturday_hours = jill_saturday_hours * 2
    john_sunday_hours = jill_sunday_hours * 3
    jill_earned = (jill_saturday_hours + jill_sunday_hours) * hourly_rate
    john_earned = (john_saturday_hours + john_sunday_hours) * hourly_rate
    difference = john_earned - jill_earned
    result = difference
    return result

print(solution())