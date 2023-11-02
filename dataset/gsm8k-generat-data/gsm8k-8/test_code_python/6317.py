def solution():
    # Calculate the total number of hours worked in April, June, and September
    april_hours = 6 * 30
    june_hours = 5 * 30
    september_hours = 8 * 30
    total_hours = april_hours + june_hours + september_hours

    # Calculate the average number of hours worked per month
    average_hours = total_hours / 3
    result = average_hours
    return result

print(solution())