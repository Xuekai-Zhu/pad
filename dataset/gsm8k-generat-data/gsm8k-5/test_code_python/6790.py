def solution():
    total_chickens = 383
    # Quentin has 25 more than double the chickens Skylar has
    q = 2*s + 25
    # Skylar has 4 less than triple the number of chickens Colten has
    s = 3*c - 4
    # Total number of chickens
    c = (total_chickens - q - s) // 3
    result = c
    return result

print(solution())