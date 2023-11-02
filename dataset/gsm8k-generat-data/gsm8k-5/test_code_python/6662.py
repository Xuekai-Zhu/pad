def solution():
    base_pay = 150  # Queenie earns $150 a day as a part-time clerk
    overtime_pay_rate = 5  # Queenie earns an additional $5 per hour as overtime pay
    overtime_hours = 4  # Queenie worked 4 hours of overtime per day
    total_days = 5  # Queenie worked 5 days

    # Calculate the total pay for working without overtime
    base_pay_total = base_pay * total_days

    # Calculate the total pay for working overtime
    overtime_pay_total = overtime_pay_rate * overtime_hours * total_days

    # Calculate the total pay for working with overtime
    total_pay = base_pay_total + overtime_pay_total
    result = total_pay
    return result

print(solution())