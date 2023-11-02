def solution():
    # Calculate the hourly pay of experienced sailors
    hourly_pay_inexperienced = 10
    hourly_pay_experienced = hourly_pay_inexperienced * (1 + 1/5)

    # Calculate the total number of hours worked by the sailors
    num_sailors = 17
    total_hours_worked = num_sailors * 60

    # Calculate the total earnings of the experienced sailors
    num_experienced_sailors = num_sailors - 5
    total_earnings_experienced = num_experienced_sailors * hourly_pay_experienced * total_hours_worked

    # Convert to monthly earnings
    total_earnings_monthly = total_earnings_experienced / 4
    result = total_earnings_monthly
    return result

print(solution())