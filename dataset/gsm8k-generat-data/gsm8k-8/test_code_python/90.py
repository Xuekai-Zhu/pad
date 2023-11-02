def solution():
    # Define the number of cups of food needed per day
    cups_per_day = 1

    # Calculate the number of cups of food needed for one month
    cups_per_month = cups_per_day * 2 * 31

    # Calculate the total number of cups of food needed for three months
    total_cups_needed = cups_per_month * 3
    result = total_cups_needed
    return result

print(solution())