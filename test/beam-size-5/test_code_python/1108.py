def solution():
    
    total_apples = 12
    peter_apples = total_apples / 4
    paul_apples = total_apples / 3
    james_apples = total_apples - peter_apples - paul_apples
    result = james_apples
    return result

print(solution())