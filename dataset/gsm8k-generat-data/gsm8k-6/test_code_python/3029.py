def solution():
    # Calculate the total number of times Mr. Roper cuts his lawn in a year
    total_cutting_times = (15 * 6) + (3 * 6)  # 15 days a month from April to September; 3 days a month from October to March
    average_cuts_per_month = total_cutting_times / 12  # divide by 12 months in a year
    result = average_cuts_per_month
    return result

print(solution())