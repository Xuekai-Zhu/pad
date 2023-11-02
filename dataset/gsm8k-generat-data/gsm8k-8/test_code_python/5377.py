def solution():
    # Define Brianne's savings for each month
    jan_savings = 10
    feb_savings = jan_savings * 2
    mar_savings = feb_savings * 2
    apr_savings = mar_savings * 2
    may_savings = apr_savings * 2

    # Calculate total savings for May
    total_savings = jan_savings + feb_savings + mar_savings + apr_savings + may_savings
    result = may_savings
    return result

print(solution())