def solution():
    """Greta worked 40 hours and was paid $12 per hour. Her friend Lisa earned $15 per hour at her job. How many hours would Lisa have to work to equal Greta's earnings for 40 hours?"""
    greta_pay = 40 * 12
    lisa_pay = 0
    lisa_hours = 0
    while lisa_pay < greta_pay:
        lisa_hours += 1
        lisa_pay = lisa_hours * 15
    result = lisa_hours
    return result

print(solution())