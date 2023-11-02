def solution():
    total_distance = 15 + 6 + 2 + 4 + 11  # Kennedy drove a total of 15+6+2+4+11 = 38 miles
    miles_per_gallon = 19  # Kennedy's car can drive 19 miles per gallon
    gallons_used = total_distance / miles_per_gallon  # Kennedy used a total of X gallons of gas
    gallons_remaining = 0  # Initializing the variable for gallons remaining

    # Calculate gallons remaining
    if gallons_used.is_integer():  # If gallons used is a whole number
        gallons_remaining = 0
    else:
        fraction = gallons_used - int(gallons_used)  # Get the decimal fraction of gallons used
        gallons_remaining = 1 - fraction  # Subtract the fraction from 1 to get the remaining gallons

    result = gallons_remaining
    return result

print(solution())