def solution():
    # Calculate the number of times Tony needs to fill the water bottle each week
    water_per_week = 72 * 7  # Tony drinks 72 ounces of water per day for 7 days in a week
    num_refills = water_per_week / 84  # Tony's water bottle can hold 84 ounces of water
    result = num_refills
    return result

print(solution())