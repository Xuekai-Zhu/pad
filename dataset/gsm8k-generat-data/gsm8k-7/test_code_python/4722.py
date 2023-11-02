def solution():
    dresses_per_day_1 = 2
    days_1 = 7
    dresses_per_day_2 = 3
    days_2 = 2
    ribbons_per_dress = 2

    # Calculate the total number of dresses sewn during the first 7 days
    total_dresses_1 = dresses_per_day_1 * days_1

    # Calculate the total number of dresses sewn during the next 2 days
    total_dresses_2 = dresses_per_day_2 * days_2

    # Calculate the total number of dresses sewn
    total_dresses = total_dresses_1 + total_dresses_2

    # Calculate the total number of ribbons used
    total_ribbons = total_dresses * ribbons_per_dress
    result = total_ribbons
    return result

print(solution())