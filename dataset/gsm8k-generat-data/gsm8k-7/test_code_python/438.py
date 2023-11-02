def solution():
    num_rainy_days = 3
    rainy_days_rain = [3, 6, 5] # mm
    total_camping_rain = sum(rainy_days_rain)
    home_rain = 26 # mm

    # Calculate the total amount of rain Greg experienced while camping
    total_camping_rain = sum(rainy_days_rain)

    # Calculate how much less rain Greg experienced while camping compared to his house
    less_rain = home_rain - total_camping_rain
    result = less_rain
    return result

print(solution())