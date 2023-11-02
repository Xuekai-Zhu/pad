def solution():
    """Janet counts 30 crows on the powerlines and 60% more hawks than crows. How many birds does she count total?"""
    crows = 30
    hawks = crows * 0.6 + crows
    total_birds = crows + hawks
    result = total_birds
    return result

print(solution())