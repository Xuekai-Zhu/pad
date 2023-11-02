def solution():
    amount_saved_per_month = 25  # John saves $25 per month
    saving_duration = 2  # John saves for 2 years
    total_savings = amount_saved_per_month * 12 * saving_duration  # Calculate the total savings

    # Subtract the amount spent on car repair from the total savings
    remaining_savings = total_savings - 400
    result = remaining_savings
    return result

print(solution())