def solution():

    # Age of Maya
    maya_age = 30 / 2
    # Drew is 5 years older than Maya
    drew_age = maya_age + 5
    # Peter is 4 years older than Drew
    peter_age = drew_age + 4
    # Jacob's age in 2 years will be half of Peter's age
    jacob_age_in_2yrs = peter_age / 2
    # Current age of Jacob
    jacob_age = jacob_age_in_2yrs - 2
    result = jacob_age
    return result

print(solution())