def solution():
    cup_capacity = 2
    cups_per_week = cup_capacity
    birdseed_stolen = 0.5
    birdseed_available = cup_capacity - birdseed_stolen
    birds_fed = birdseed_available * 14
    result = birds_fed
    return result

print(solution())