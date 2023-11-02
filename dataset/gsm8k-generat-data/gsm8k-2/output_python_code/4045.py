def solution():
    """Sam earns $10 an hour on Math tutoring. For the first month, he earned $200; and for the second month, he earned $150 more than the first month. How many hours did he spend on tutoring for two months?"""
    first_month_pay = 200
    second_month_pay = first_month_pay + 150
    hourly_rate = 10
    first_month_hours = first_month_pay/hourly_rate
    second_month_hours = second_month_pay/hourly_rate
    total_hours = first_month_hours + second_month_hours
    result = total_hours
    return result

print(solution())