def solution():
    """In a jar that has 50 ants, the number of ants in the jar doubles each hour. How many ants will be in the jar after 5 hours?"""
    start_ants = 50
    hours = 5
    total_ants = start_ants * (2**hours)
    result = total_ants
    return result

print(solution())