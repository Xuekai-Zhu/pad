def solution():
    # Define the roles and rituals of rabbis and Christians
    rabbi_role = "spiritual leader"
    christian_ritual = "baptism"
    # Check if a rabbi can perform the Christian ritual for salvation
    if christian_ritual not in rabbi_role:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())