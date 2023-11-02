def solution():
    """Renaldo drove 15 kilometers. Ernesto drove 7 kilometers more than one-third of Renaldo's distance. How many kilometers did the 2 men drive in total?"""
    renaldo_distance = 15
    ernesto_distance = (1/3) * renaldo_distance + 7
    total_distance = renaldo_distance + ernesto_distance
    result = total_distance
    return result

print(solution())