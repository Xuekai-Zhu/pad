def solution():
    water_goal = 1.5  # Mary wants to drink 1.5 liters of water per day
    glass_size = 0.25  # Each glass holds 250 mL of water
    glasses_per_day = water_goal / glass_size  # Calculate the number of glasses Mary needs to drink

    result = glasses_per_day
    return result

print(solution())