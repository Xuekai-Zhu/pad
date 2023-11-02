def solution():
    
    mark_sandcastles = 20
    mark_towers_per_sandcastle = 10
    jeff_sandcastles = 3 * mark_sandcastles
    jeff_towers_per_sandcastle = 5
    total_sandcastles = mark_sandcastles + jeff_sandcastles
    total_towers = (mark_sandcastles * mark_towers_per_sandcastle) + (jeff_sandcastles * jeff_towers_per_sandcastle)
    result = total_sandcastles + total_towers
    return result

print(solution())