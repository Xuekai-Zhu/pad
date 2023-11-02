def solution():
    """There are 11 boys and 13 girls in a class. If 1 boy is added to the class, what percentage of the class are girls?"""
    boys = 11
    girls = 13
    total_students = boys + girls + 1
    percentage_girls = (girls / total_students) * 100
    result = percentage_girls
    return result

print(solution())