def solution():
    """Jamie earns $20 per hour for 8 hours of work each day. Should she need to work additional hours, she is paid a special hourly rate that is 150% of her regular hourly rate. Last Tuesday, she worked 11 hours. How much was she paid, in dollars, for her work that day?"""
    regular_pay = 20 * 8
    overtime_pay = (20 * 1.5) * 3
    total_pay = regular_pay + overtime_pay
    result = total_pay
    return result

print(solution())