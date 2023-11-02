def solution():
    """Drew is 5 years older than Maya. Peter is 4 years older than Drew. John is 30 and is twice as old as Maya. In 2 years, Jacob will be exactly half of Peter's age. How old is Jacob now?"""
    # Let Maya's age be x
    maya_age = x
    # Drew is 5 years older than Maya
    drew_age = x + 5
    # Peter is 4 years older than Drew
    peter_age = drew_age + 4
    # John is 30 and is twice as old as Maya
    john_age = 30
    maya_age = john_age / 2
    # In 2 years, Jacob will be exactly half of Peter's age
    jacob_age = (peter_age + 2) / 2 - 2
    result = jacob_age
    return result

print(solution())