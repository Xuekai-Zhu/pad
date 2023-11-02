def solution():
    """Gina can paint six cups an hour with roses and 7 cups an hour with lilies. Her Etsy store gets an order for 6 rose cups and 14 lily cups. If Gina gets paid $90 total for the order, how much does she make per hour?"""
    rose_cups_per_hour = 6
    lily_cups_per_hour = 7
    total_cups_ordered = 6 + 14
    hours_to_complete_order = total_cups_ordered / (rose_cups_per_hour + lily_cups_per_hour)
    total_pay = 90
    pay_per_hour = total_pay / hours_to_complete_order
    result = pay_per_hour
    return result

print(solution())