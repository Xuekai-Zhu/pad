def solution():
    
    wallace_capacity = 40
    wallace_level = 3/4
    catherine_capacity = wallace_capacity / 2
    catherine_level = 3/4
    total_gallons = wallace_capacity * wallace_level + catherine_capacity * catherine_level
    result = total_gallons
    return result

print(solution())