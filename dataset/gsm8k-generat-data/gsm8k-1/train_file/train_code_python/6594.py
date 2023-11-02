def solution():
    """Drew is 5 years older than Maya. Peter is 4 years older than Drew. John is 30 and is twice as old as Maya. In 2 years, Jacob will be exactly half of Peter’s age. How old is Jacob now?"""
    # Let's first find the age of Maya
    maya_age = 30 // 2  # John is 30 and is twice as old as Maya
    # Drew is 5 years older than Maya
    drew_age = maya_age + 5
    # Peter is 4 years older than Drew
    peter_age = drew_age + 4
    # In 2 years, Jacob will be exactly half of Peter’s age
    jacob_age_after_two_years = (peter_age + 2) / 2
    # Let's calculate Jacob's current age by subtracting 2 from his age 2 years later
    jacob_age = jacob_age_after_two_years - 2
    result = jacob_age
    return result

print(solution())