def solution():
    """Brittany uses 1/4 ounce of shampoo to wash her hair every other day. She buys shampoo in 14-ounce bottles. How many bottles does she need to get her through a leap year?"""
    # Define the amount of shampoo Brittany uses in a day
    shampoo_per_day = 1 / 8  # since she washes every other day

    # Define the number of days in a leap year
    days_in_leap_year = 366

    # Calculate the total amount of shampoo Brittany will need for the year
    shampoo_needed = shampoo_per_day * days_in_leap_year

    # Calculate the number of bottles of shampoo Brittany will need to buy
    bottles_needed = shampoo_needed / 14

    # Round up to the nearest whole number of bottles
    bottles_needed = math.ceil(bottles_needed)

    # Display the number of bottles Brittany will need to buy
    result = bottles_needed
    return result

print(solution())