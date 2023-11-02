def solution():
    """Al is 25 pounds heavier than Ben. Ben is 16 pounds lighter than Carl. If Ed weighs 146 pounds and is 38 pounds lighter than Al, find the weight of Carl."""
    ed_weight = 146
    al_weight = ed_weight + 38
    ben_weight = al_weight - 25
    carl_weight = ben_weight + 16
    result = carl_weight
    return result

print(solution())