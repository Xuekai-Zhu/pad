def solution():
    
    feeder_capacity = 2
    birds_per_cup = 14
    squirrel_steal = 0.5
    remaining_birdseed = feeder_capacity - squirrel_steal
    birds_per_week = remaining_birdseed * birds_per_cup
    result = birds_per_week
    return result

print(solution())