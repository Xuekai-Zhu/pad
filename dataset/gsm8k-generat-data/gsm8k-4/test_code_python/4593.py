def solution():
    """Brittany uses 1/4 ounce of shampoo to wash her hair every other day. She buys shampoo in 14-ounce bottles. How many bottles does she need to get her through a leap year?"""
    # Define the amount of shampoo used per day
    shampoo_per_day = 1 / 8  # 1/4 ounce every other day = 1/8 ounce per day

    # Define the number of days in a leap year
    days_in_leap_year = 366

    # Calculate the total amount of shampoo needed for a leap year
    total_shampoo_needed = shampoo_per_day * days_in_leap_year

    # Calculate the number of bottles needed
    bottles_needed = total_shampoo_needed / 14

    # Round up to the nearest whole number of bottles
    bottles_needed = math.ceil(bottles_needed)

    # Return the result
    return bottles_needed

print(solution())