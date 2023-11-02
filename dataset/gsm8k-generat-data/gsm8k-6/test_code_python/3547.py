def solution():
    # Find the total number of gallons James can transport
    gallons_2trucks = 2 * 8000  # the first 2 trucks are 8000 gallons each
    gallons_3rdtruck = 0.7 * gallons_2trucks  # the 3rd truck is 30% less than the first 2 trucks
    gallons_remaining = 3 * gallons_2trucks  # the remaining 3 trucks are 50% larger than the first 2 trucks
    total_gallons = gallons_2trucks + gallons_3rdtruck + gallons_remaining
    result = total_gallons
    return result

print(solution())