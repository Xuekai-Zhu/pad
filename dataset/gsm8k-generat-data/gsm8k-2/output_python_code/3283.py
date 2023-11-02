def solution():
    """Antonella has ten Canadian coins in her purse that are either loonies or toonies. A loonie equals $1 and a toonie equals $2. If she bought a $3 Frappuccino and still has $11, how many toonies did she initially have?"""
    total_value = 11 + 3
    loonies = range(0, 11)
    toonies = range(0, 11)
    toonies_initial = 0
    for loonie_count in loonies:
        for toonie_count in toonies:
            if loonie_count + toonie_count == 10 and (loonie_count + 2 * toonie_count) - total_value // 2 == 0:
                toonies_initial = toonie_count
                break
    result = toonies_initial
    return result

print(solution())