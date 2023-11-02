def solution():
    """Greta worked 40 hours and was paid $12 per hour. Her friend Lisa earned $15 per hour at her job. How many hours would Lisa have to work to equal Greta's earnings for 40 hours?"""
    greta_pay = 40 * 12
    lisa_hourly_pay = 15
    lisa_hours_to_equal_greta = greta_pay / lisa_hourly_pay
    result = lisa_hours_to_equal_greta
    return result

print(solution())