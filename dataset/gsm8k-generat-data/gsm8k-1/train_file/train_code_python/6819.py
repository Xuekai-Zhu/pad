def solution():
    """Jade and Krista went on a road trip for 3 days. On each day Jade had to drive 8 hours and Krista had to drive 6 hours to arrive at the destination. How many hours did they drive altogether?"""
    jade_hours_per_day = 8
    krista_hours_per_day = 6
    days = 3
    total_hours = (jade_hours_per_day + krista_hours_per_day) * days
    result = total_hours
    return result

print(solution())