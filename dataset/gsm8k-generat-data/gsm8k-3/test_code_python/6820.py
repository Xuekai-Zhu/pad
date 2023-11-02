def solution():
    """Jade and Krista went on a road trip for 3 days. On each day Jade had to drive 8 hours and Krista had to drive 6 hours to arrive at the destination. How many hours did they drive altogether?"""
    # Define the number of days on the road trip
    DAYS = 3

    # Define the number of hours Jade and Krista drive each day
    JADE_HOURS = 8
    KRISTA_HOURS = 6

    # Calculate the total number of hours Jade and Krista drove
    total_hours = (JADE_HOURS + KRISTA_HOURS) * DAYS

    # Display the total number of hours driven
    result = total_hours
    return result

print(solution())