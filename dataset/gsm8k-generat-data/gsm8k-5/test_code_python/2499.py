def solution():
    loaves_start_day = 2355  # Supermarket has 2355 loaves of bread at the start of the day
    loaves_sold = 629  # 629 loaves are sold by afternoon
    loaves_delivered = 489  # 489 loaves are delivered by the supplier in the evening

    # Calculate the total number of loaves of bread at the end of the day
    loaves_end_day = loaves_start_day - loaves_sold + loaves_delivered
    result = loaves_end_day
    return result

print(solution())