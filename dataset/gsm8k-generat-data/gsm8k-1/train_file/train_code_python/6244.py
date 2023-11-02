def solution():
    """Shawna has 7 acorns. Sheila has 5 times as many acorns as Shawna, but 3 fewer acorns than Danny. How many acorns do they have altogether?"""
    shawna_acorns = 7
    sheila_acorns = shawna_acorns * 5
    danny_acorns = sheila_acorns + 3
    total_acorns = shawna_acorns + sheila_acorns + danny_acorns
    result = total_acorns
    return result

print(solution())