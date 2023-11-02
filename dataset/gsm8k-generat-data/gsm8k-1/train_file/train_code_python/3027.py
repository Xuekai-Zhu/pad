def solution():
    """There are 20 sandcastles on Mark's beach, each with 10 towers. On Jeff's beach, there are three times as many castles as on Mark's beach, each with 5 towers. What is the combined total number of sandcastles and towers on Mark's and Jeff's beaches?"""
    mark_castles = 20
    mark_towers = 10
    mark_total = mark_castles * mark_towers
    jeff_castles = mark_castles * 3
    jeff_towers = 5
    jeff_total = jeff_castles * jeff_towers
    result = mark_total + jeff_total
    return result

print(solution())