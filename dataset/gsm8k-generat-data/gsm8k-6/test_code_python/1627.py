def solution():
    # Calculate the total amount of water filled in the pool in the first 3 hours
    water_filled_initially = 50 * 3  # hose sprays 50 gallons per hour, so in 3 hours, it fills 50*3 = 150 gallons

    # Calculate the remaining amount of water to be filled in the pool
    remaining_water = 0  # initially the pool is empty
    time_for_second_hose = 2  # additional 2 hours with both hoses
    rate_of_second_hose = 70  # second hose sprays 70 gallons per hour
    rate_of_both_hoses = 50 + 70  # total rate when both hoses are used
    remaining_time = time_for_second_hose * rate_of_both_hoses  # total gallons of water filled in 2 hours with both hoses
    remaining_water = remaining_time + water_filled_initially   # total amount of water filled in the pool

    result = remaining_water
    return result

print(solution())