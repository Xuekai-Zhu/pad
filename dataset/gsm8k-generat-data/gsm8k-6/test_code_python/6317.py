def solution():
    # Calculate the total number of hours worked by Brady in those 3 months
    total_hours = 6*30 + 5*30 + 8*30  # Brady worked 6 hours/day in April, 5 hours/day in June, and 8 hours/day in September
    average_hours = total_hours / 3  # calculate the average hours worked per month
    result = average_hours
    return result

print(solution())