def solution():
    # Calculate how many inches Alex needs to grow in one year
    inches_needed = 54 - 48

    # Calculate how many inches Alex can grow in one year without hanging upside down
    normal_growth = 12 * (1/3)

    # Calculate how many inches Alex needs to grow by hanging upside down
    hanging_growth = inches_needed - normal_growth

    # Calculate how many hours Alex needs to hang upside down each month to achieve the required growth
    hours_per_month = hanging_growth / (1/12)

    result = hours_per_month
    return result

print(solution())