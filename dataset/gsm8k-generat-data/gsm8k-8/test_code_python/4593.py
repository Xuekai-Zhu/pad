def solution():
    # Calculate the amount of shampoo used in a year
    shampoo_per_day = 1/4
    shampoo_per_year = shampoo_per_day * 182.5 # 365 days in a year, but every other day
    bottles_needed = shampoo_per_year / 14 # 14-ounce bottles

    # Round up to the nearest whole number
    bottles_needed = math.ceil(bottles_needed)

    result = bottles_needed
    return result

print(solution())