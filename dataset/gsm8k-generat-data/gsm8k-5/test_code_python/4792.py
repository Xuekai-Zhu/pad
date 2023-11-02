def solution():
    pots_on_monday = 12
    pots_on_tuesday = pots_on_monday * 2
    total_pots = pots_on_monday + pots_on_tuesday

    # Let's assume Nancy created x pots on Wednesday
    # Since she ended the week with 50 pots, we can set up the equation:
    # total_pots + x = 50
    # Solving for x:
    x = 50 - total_pots

    # Nancy created x pots on Wednesday
    result = x
    return result

print(solution())