def solution():
    """A cleaning company produces two sanitizer sprays. One spray kills 50% of germs, and another spray kills 25% of germs. However, 5% of the germs they kill are the same ones. What percentage of germs would be left after using both sanitizer sprays together?"""
    spray1 = 0.5
    spray2 = 0.25
    shared_kills = 0.05
    total_kills = spray1 + spray2 - (spray1 * shared_kills)
    percent_left = (1 - total_kills) * 100
    result = percent_left
    return result

print(solution())