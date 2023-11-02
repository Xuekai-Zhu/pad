def solution():
    crows = 30  # Janet counts 30 crows
    hawks = int(crows * 0.6) + crows  # Janet counts 60% more hawks than crows, so she counts crows + 60% of crows = 1.6 * crows
    total_birds = crows + hawks  # Janet counts crows + hawks
    result = total_birds
    return result

print(solution())