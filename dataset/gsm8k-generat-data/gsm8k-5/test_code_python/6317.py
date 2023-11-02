def solution():
    april_hours = 6 * 30  # Brady worked 6 hours every day in April
    june_hours = 5 * 30  # Brady worked 5 hours every day in June
    september_hours = 8 * 30  # Brady worked 8 hours every day in September

    # Calculate the total number of hours Brady worked in those 3 months
    total_hours = april_hours + june_hours + september_hours

    # Calculate the average number of hours Brady worked per month in those 3 months
    average_hours_per_month = total_hours / 3
    result = average_hours_per_month
    return result

print(solution())