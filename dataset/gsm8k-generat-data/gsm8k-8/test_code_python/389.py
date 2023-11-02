def solution():
    # Define the variables
    first_half_days = 15
    first_half_rain = 4
    remaining_days = 30 - first_half_days
    remaining_rain = first_half_rain * 2

    # Calculate the total rainfall
    total_rain = (first_half_days * first_half_rain) + (remaining_days * remaining_rain)
    result = total_rain
    return result

print(solution())