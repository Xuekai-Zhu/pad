def solution():
    """Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?"""
    babysitting_time = 50/60 # convert minutes to hours
    hourly_rate = 12
    payment = babysitting_time * hourly_rate
    result = payment
    return result

print(solution())