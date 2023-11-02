def solution():
    """Queenie earns $150 a day as a part-time clerk. She earns an additional $5 per hour as overtime pay. How much will Queenie receive for working 5 days with 4 hours overtime?"""
    part_time_pay = 150 * 5
    overtime_pay = 5 * 4 * 5
    total_pay = part_time_pay + overtime_pay
    result = total_pay
    return result

print(solution())