def solution():
    num_months = 12
    num_lawn_cuttings_spring_summer = 15 * 6  # April to September, 15 days per month
    num_lawn_cuttings_fall_winter = 3 * 6  # October to March, 3 days per month

    # Calculate the total number of lawn cuttings for the year
    total_lawn_cuttings = num_lawn_cuttings_spring_summer + num_lawn_cuttings_fall_winter

    # Calculate the average number of lawn cuttings per month
    avg_lawn_cuttings = total_lawn_cuttings / num_months
    result = avg_lawn_cuttings
    return result

print(solution())