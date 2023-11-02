def solution():
    """Derek finally gets his own allowance. He puts $2 away in January, $4 away in February, $8 away in March, $16 away in April and follows this savings pattern through to December. How much money does he have to spare and save by December?"""
    jan_savings = 2
    feb_savings = 4
    mar_savings = 8
    apr_savings = 16
    total_savings = jan_savings + feb_savings + mar_savings + apr_savings
    for i in range(5, 13):
        month_savings = apr_savings * 2
        total_savings += month_savings
    
    result = total_savings
    return result

print(solution())