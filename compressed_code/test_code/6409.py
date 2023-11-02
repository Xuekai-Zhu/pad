def solution():
    
    birdseed_capacity = 2
    birdseed_needed = 1
    birds_per_cup = 14
    squirrel_steals = 0.5
    birdseed_per_week = birdseed_capacity - squirrel_steals
    total_birds = birdseed_per_week * birds_per_cup
    result = total_birds
    return result

print(solution())