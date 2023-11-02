def solution():
    daughters = 3
    sons = 3
    sons_per_daughter = 6
    daughters_per_son = 5
    total_grandchildren = (daughters * sons_per_daughter) + (sons * daughters_per_son)
    result = total_grandchildren
    return result

print(solution())