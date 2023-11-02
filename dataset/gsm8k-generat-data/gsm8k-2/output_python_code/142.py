def solution():
    """A cleaning company produces two sanitizer sprays. One spray kills 50% of germs, and another spray kills 25% of germs. However, 5% of the germs they kill are the same ones. What percentage of germs would be left after using both sanitizer sprays together?"""
    germ1_killed = 0.5
    germ2_killed = 0.25
    overlapping_killed = 0.05
    remaining_germs = 1 - ((1 - germ1_killed) * (1 - germ2_killed - overlapping_killed))
    result = remaining_germs * 100
    return result

print(solution())