def solution():
    """Greta worked 40 hours and was paid $12 per hour. Her friend Lisa earned $15 per hour at her job. How many hours would Lisa have to work to equal Greta's earnings for 40 hours?"""
    # Define Greta's pay rate and hours worked
    greta_pay = 12
    greta_hours = 40

    # Calculate Greta's total earnings
    greta_earnings = greta_pay * greta_hours

    # Calculate Lisa's pay rate needed to equal Greta's earnings
    lisa_pay = greta_earnings / 40 / 15

    # Calculate the number of hours Lisa would need to work at her pay rate to equal Greta's earnings
    lisa_hours = greta_earnings / (lisa_pay * 40)

    # return the result
    result = lisa_hours
    return result

print(solution())