def solution():
    """On their way driving to Los Angeles, Benjamin and James see lots of billboard ads. Curious, Benjamin starts to count how many they see. In the first hour once he starts counting he counts 17 billboards. In the second hour once he starts counting he sees 20 billboards. In the third hour he sees 23 billboards. James asks Benjamin the average number of billboards they've seen per hour. What should Benjamin tell him?"""
    total_billboards = 17 + 20 + 23
    hours = 3
    average_billboards = total_billboards / hours
    result = average_billboards
    return result

print(solution())