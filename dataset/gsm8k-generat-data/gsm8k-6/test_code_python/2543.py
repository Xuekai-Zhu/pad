def solution():
    # Calculate the number of glasses of water Matthew drinks per week
    glasses_per_week = 4 * 7  # Matthew drinks 4 glasses of water per day for 7 days per week
    ounces_per_glass = 5  # each glass of water is 5 ounces
    total_ounces_per_week = glasses_per_week * ounces_per_glass  # total ounces of water Matthew drinks per week
    water_bottle_size = 35  # Matthew buys a 35 ounces water bottle
    num_refills_per_week = total_ounces_per_week // water_bottle_size  # calculate the number of times he will fill the bottle each week
    result = num_refills_per_week
    return result

print(solution())