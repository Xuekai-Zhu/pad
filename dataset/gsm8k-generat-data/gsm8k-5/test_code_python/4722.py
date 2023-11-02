def solution():
    dresses_per_day_1 = 2  # Jane sews 2 dresses per day for the first 7 days
    dresses_per_day_2 = 3  # Jane sews 3 dresses per day for the next 2 days
    days_1 = 7  # Jane sews 2 dresses per day for the first 7 days
    days_2 = 2  # Jane sews 3 dresses per day for the next 2 days
    ribbons_per_dress = 2  # Jane adds 2 ribbons to each dress

    # Calculate the total number of dresses Jane sews
    total_dresses = (dresses_per_day_1 * days_1) + (dresses_per_day_2 * days_2)

    # Calculate the total number of ribbons Jane uses
    total_ribbons = total_dresses * ribbons_per_dress
    result = total_ribbons
    return result

print(solution())