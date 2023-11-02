def solution():
    # Find Maya's age
    maya_age = 30 / 2  # John is twice as old as Maya
    
    # Find Drew's age
    drew_age = maya_age + 5  # Drew is 5 years older than Maya
    
    # Find Peter's age
    peter_age = drew_age + 4  # Peter is 4 years older than Drew
    
    # Find Jacob's age
    jacob_age = (peter_age + 2) / 2  # In 2 years, Jacob will be exactly half of Peter’s age
    
    result = jacob_age
    return result

print(solution())