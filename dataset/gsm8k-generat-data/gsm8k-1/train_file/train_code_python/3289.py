def solution():
    """Working together, four pugs can clean their house in 45 minutes. In how many minutes will 15 pugs working together be able to clean their house?"""
    pugs_1 = 4
    time_1 = 45
    pugs_2 = 15
    time_2 = (pugs_1 * time_1) / pugs_2
    result = time_2
    return result

print(solution())