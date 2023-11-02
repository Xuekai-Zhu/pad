def solution():
    """
    Alex needs to be 54 inches tall to ride the newest roller coaster at the theme park.
    He is 48 inches tall this year. For every hour he hangs upside down, he can grow 1/12 of an inch.
    Normally he grows 1/3 of an inch per month. On average, how many hours does he need to hang upside down each month
    to be tall enough next year to ride the rollercoaster?
    """
    # Calculate how many inches Alex needs to grow in total
    inches_to_grow = 54 - 48

    # Calculate how many inches Alex can grow in a year from normal growth
    normal_growth = 12 * (1/3)

    # Calculate how many inches Alex needs to grow from hanging upside down
    hanging_growth = inches_to_grow - normal_growth

    # Calculate how many hours Alex needs to hang upside down each month to reach his goal
    hours_per_month = hanging_growth / (1/12)

    # Display the average hours per month needed to hang upside down
    result = hours_per_month
    return result

print(solution())