def solution():
    # Calculate the total amount of money Derek saves by December
    jan_savings = 2
    feb_savings = 4
    mar_savings = 8
    apr_savings = 16
    total_savings = jan_savings + feb_savings + mar_savings + apr_savings  # add the first four months' savings

    # Calculate the savings for the remaining 8 months using a loop
    for i in range(5, 13):
        month_savings = 2 * apr_savings  # double the savings of the previous month
        total_savings += month_savings  # add the savings for the current month

    result = total_savings
    return result

print(solution())