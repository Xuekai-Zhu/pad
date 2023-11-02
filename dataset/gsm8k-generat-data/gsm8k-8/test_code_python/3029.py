def solution():
    # Calculate the number of months Mr. Roper cuts his lawn from April to September
    months_april_to_sept = 6
    days_per_month = 15
    times_per_month_april_to_sept = months_april_to_sept * days_per_month

    # Calculate the number of times Mr. Roper cuts his lawn from October to March
    times_per_month_oct_to_march = 3

    # Calculate the total number of times Mr. Roper cuts his lawn
    total_times_cut = times_per_month_april_to_sept + times_per_month_oct_to_march

    # Calculate the average number of times Mr. Roper cuts his lawn per month
    num_months = 12
    avg_times_cut_per_month = total_times_cut / num_months

    result = avg_times_cut_per_month
    return result

print(solution())