def solution():
    num_vans = 6

    # Calculate the total gallons for the first 2 vans
    gallons_first_two_vans = 2 * 8000

    # Calculate the gallons for the third van, which is 30% less than the first two
    gallons_third_van = 0.7 * gallons_first_two_vans

    # Calculate the total gallons for the first three vans
    total_gallons_first_three_vans = gallons_first_two_vans + gallons_third_van

    # Calculate the gallons for the remaining three vans, which are 50% larger than the first two
    gallons_remaining_vans = 3 * 1.5 * 8000

    # Calculate the total gallons for all six vans
    total_gallons = total_gallons_first_three_vans + gallons_remaining_vans
    result = total_gallons
    return result

print(solution())