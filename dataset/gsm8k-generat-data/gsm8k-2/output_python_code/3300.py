def solution():
    """Quinn catches twice the amount of frogs as Alster who caught 2. Bret catches three times the amount of frogs as Quinn. How many frogs did Bret catch?"""
    alster_frogs = 2
    quinn_frogs = 2 * alster_frogs
    bret_frogs = 3 * quinn_frogs
    total_frogs = alster_frogs + quinn_frogs + bret_frogs
    result = bret_frogs
    return result

print(solution())