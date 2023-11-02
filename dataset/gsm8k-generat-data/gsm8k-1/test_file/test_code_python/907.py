def solution():
    """Colby works for a manufacturing company in the packaging division. He gets paid $0.20 for every package he completes. If he completes 10 less than 50 packages per hour, how much money, in dollars, does he earn in a typical eight-hour workday?"""
    packages_per_hour = 50 - 10
    hours_worked = 8
    pay_per_package = 0.20
    total_packages = packages_per_hour * hours_worked
    total_pay = total_packages * pay_per_package
    result = total_pay
    return result

print(solution())