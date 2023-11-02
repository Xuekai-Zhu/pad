def solution():
    """Building A has 4 floors, which is 9 less than Building B. Building C has six less than five times as many floors as Building B. How many floors does Building C have?"""
    b_floors = 4 + 9
    c_floors = (5 * b_floors) - 6
    result = c_floors
    return result

print(solution())