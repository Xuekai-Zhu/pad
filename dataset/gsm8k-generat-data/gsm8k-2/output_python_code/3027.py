def solution():
    """There are 20 sandcastles on Mark's beach, each with 10 towers. On Jeff's beach, there are three times as many castles as on Mark's beach, each with 5 towers. What is the combined total number of sandcastles and towers on Mark's and Jeff's beaches?"""
    mark_sandcastles = 20
    mark_towers_per_sandcastle = 10
    jeff_sandcastles = 3 * mark_sandcastles
    jeff_towers_per_sandcastle = 5
    total_sandcastles = mark_sandcastles + jeff_sandcastles
    total_towers = (mark_sandcastles * mark_towers_per_sandcastle) + (jeff_sandcastles * jeff_towers_per_sandcastle)
    result = total_sandcastles + total_towers
    return result

print(solution())