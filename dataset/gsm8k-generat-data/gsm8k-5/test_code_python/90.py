def solution():
    cups_per_day = 1  # Herman feeds the birds 1 cup of food per day
    days_in_month = 31  # Assuming there are 31 days in each month
    months = 3  # Herman feeds the birds for 3 months

    # Calculate the total cups of food needed for all 3 months
    total_cups_needed = cups_per_day * 2 * days_in_month * months

    result = total_cups_needed
    return result

print(solution())