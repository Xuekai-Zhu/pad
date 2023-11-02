def solution():
    """To improve her health, Mary decides to drink 1.5 liters of water a day as recommended by her doctor. Mary's glasses hold 250 mL of water. How many glasses of water should Mary drink per day to reach her goal?"""
    liters_per_day = 1.5
    ml_per_glass = 250
    glasses_per_day = int(liters_per_day * 1000 / ml_per_glass)
    result = glasses_per_day
    return result

print(solution())