def solution():
    """Jade and Krista went on a road trip for 3 days. On each day Jade had to drive 8 hours and Krista had to drive 6 hours to arrive at the destination. How many hours did they drive altogether?"""
    # Define the number of days
    num_days = 3

    # Define the number of hours each person drives per day
    jade_hours_per_day = 8
    krista_hours_per_day = 6

    # Calculate the total number of hours Jade and Krista drove together
    total_hours = (jade_hours_per_day + krista_hours_per_day) * num_days

    # return the result
    result = total_hours
    return result

print(solution())