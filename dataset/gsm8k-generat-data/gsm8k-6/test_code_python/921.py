def solution():
    # Calculate the number of guests who drank soda, sparkling water, and juice
    num_soda_drinkers = 90 * 1/2  # one-half of the guests drank soda
    num_sparkling_water_drinkers = 90 * 1/3  # one-third of the guests drank sparkling water
    num_juice_drinkers = 90 - num_soda_drinkers - num_sparkling_water_drinkers  # the remaining guests drank juice

    # Calculate the number of glass bottles of juice that were consumed
    num_juice_bottles_consumed = 50 * 4/5  # four-fifths of the juice bottles were consumed

    # Calculate the total number of recyclable cans and bottles collected
    total_recyclable = (50 - num_juice_bottles_consumed) + (num_soda_drinkers * 1) + (num_sparkling_water_drinkers * 1)
    result = total_recyclable
    return result

print(solution())