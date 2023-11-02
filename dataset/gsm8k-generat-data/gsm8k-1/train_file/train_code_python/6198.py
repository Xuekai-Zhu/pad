def solution():
    """Building A has 4 floors, which is 9 less than Building B. Building C has six less than five times as many floors as Building B. How many floors does Building C have?"""
    floors_b = 4 + 9
    floors_c = (5 * floors_b) - 6
    result = floors_c
    return result

print(solution())