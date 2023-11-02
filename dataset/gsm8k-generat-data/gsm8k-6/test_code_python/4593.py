def solution():
    # Calculate the total amount of shampoo Brittany needs in a leap year
    shampoo_needed = 1/4 * 183  # a leap year has 366 days, and Brittany washes her hair every other day
    bottles_needed = shampoo_needed / 14  # calculate the number of bottles needed
    result = math.ceil(bottles_needed)  # round up to the nearest integer
    return result

print(solution())