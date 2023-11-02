def solution():
    # Calculate the gallons in the first two vans
    gallons_first_two = 2 * 8000  # 2 vans with 8000 gallons each

    # Calculate the gallons in the third van
    gallons_third = 0.7 * 8000  # 30% less than the first two vans

    # Calculate the total gallons in the first three vans
    total_gallons_first_three = gallons_first_two + gallons_third

    # Calculate the gallons in the remaining three vans
    gallons_remaining = 1.5 * gallons_first_two  # 50% larger than the first two vans

    # Calculate the total gallons in all six vans
    total_gallons = total_gallons_first_three + gallons_remaining
    result = total_gallons
    return result

print(solution())