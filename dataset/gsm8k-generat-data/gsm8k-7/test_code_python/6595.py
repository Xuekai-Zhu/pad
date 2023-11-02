def solution():
    john_age = 30
    maya_age = john_age / 2
    drew_age = maya_age + 5
    peter_age = drew_age + 4
    
    # Determine Jacob's current age
    jacob_age = peter_age - 2 * 0.5
    
    result = jacob_age
    return result

print(solution())