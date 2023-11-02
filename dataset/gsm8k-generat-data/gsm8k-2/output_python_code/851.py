def solution():
    """In a jar that has 50 ants, the number of ants in the jar doubles each hour. How many ants will be in the jar after 5 hours?"""
    ants_in_jar = 50
    for i in range(5):
        ants_in_jar *= 2
    result = ants_in_jar
    return result

print(solution())