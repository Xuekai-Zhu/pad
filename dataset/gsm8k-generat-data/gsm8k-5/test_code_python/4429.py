def solution():
    water_per_day = 2.5  # Ivy drinks 2.5 liters of water each day
    days = 4  # Ivy wants to buy enough water for 4 days

    # Calculate the total amount of water Ivy will drink in 4 days
    total_water = water_per_day * days

    # Convert the total amount of water to the number of 2-liter water bottles
    bottles_needed = total_water / 2
    result = bottles_needed
    return result

print(solution())