def solution():
    # Calculate Brianne's savings for February, March, April, and May
    feb_savings = 2 * 10  # twice as much as January's savings
    mar_savings = 2 * feb_savings
    apr_savings = 2 * mar_savings
    may_savings = 2 * apr_savings
    total_savings = 10 + feb_savings + mar_savings + apr_savings + may_savings  # total savings from January to May
    result = may_savings
    return result

print(solution())