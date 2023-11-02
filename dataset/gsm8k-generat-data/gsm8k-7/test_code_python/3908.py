def solution():
    baths_per_week = 2
    showers_per_week = 1
    weeks_in_year = 52

    # Calculate the total number of times Michael takes a bath
    total_baths = baths_per_week * weeks_in_year

    # Calculate the total number of times Michael takes a shower
    total_showers = showers_per_week * weeks_in_year

    # Calculate the total number of times Michael cleans himself
    total_cleaning = total_baths + total_showers
    result = total_cleaning
    return result

print(solution())