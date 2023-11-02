def solution():
    daily_allowance = 12  # Martha receives a daily allowance of $12
    weekly_allowance = daily_allowance * 7  # Martha's weekly allowance is $12 x 7 days = $84
    weekly_savings = ((daily_allowance / 2) * 6) + ((daily_allowance / 4) * 1)
    # Martha saves half of her daily allowance for 6 days and a quarter for 1 day
    total_savings = weekly_savings

    # Return the total amount saved at the end of the week
    result = total_savings
    return result

print(solution())