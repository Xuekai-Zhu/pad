def solution():
    """There are 11 boys and 13 girls in a class. If 1 boy is added to the class, what percentage of the class are girls?"""
    boys_initial = 11
    girls_initial = 13
    total_initial = boys_initial + girls_initial
    boys_after = boys_initial + 1
    total_after = boys_after + girls_initial
    percent_girls = (girls_initial / total_initial) * 100
    result = percent_girls
    return result

print(solution())