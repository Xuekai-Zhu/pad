def solution():
    total_water = 60  # Gumball drank 60 liters of water for the week
    water_per_day = (9*3 + 8*3)  # Gumball drank 9 liters on 3 days and 8 liters on 3 days
    water_missing = total_water - water_per_day  # Gumball did not input the data for one day

    # Calculate how many liters of water Gumball drank on Wednesday
    water_on_wednesday = water_missing / 1
    result = water_on_wednesday
    return result

print(solution())