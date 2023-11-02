def solution():
    alster_catches = 2  # Alster catches 2 frogs
    quinn_catches = 2 * 2  # Quinn catches twice the amount of frogs as Alster
    bret_catches = 3 * quinn_catches  # Bret catches three times the amount of frogs as Quinn

    total_frogs = alster_catches + quinn_catches + bret_catches
    result = bret_catches
    return result

print(solution())