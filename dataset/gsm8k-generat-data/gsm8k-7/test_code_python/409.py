def solution():
    total_days = 30
    quota = 50
    cars_sold = 0

    # Calculate the number of cars sold in the first 3 days
    cars_sold += 5 * 3

    # Calculate the number of cars sold in the next 4 days
    cars_sold += 3 * 4

    # Calculate the number of remaining days
    remaining_days = total_days - 7

    # Calculate the average number of cars Frank needs to sell per day to meet his quota
    avg_cars_per_day = (quota - cars_sold) / remaining_days

    result = avg_cars_per_day
    return result

print(solution())