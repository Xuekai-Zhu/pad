def solution():
    """Sam earns $10 an hour on Math tutoring. For the first month, he earned $200; and for the second month, he earned $150 more than the first month. How many hours did he spend on tutoring for two months?"""
    first_month_income = 200
    second_month_income = first_month_income + 150
    total_income = first_month_income + second_month_income
    hourly_rate = 10
    total_hours = total_income / hourly_rate
    result = total_hours
    return result

print(solution())