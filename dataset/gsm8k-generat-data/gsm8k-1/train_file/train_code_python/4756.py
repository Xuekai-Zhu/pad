def solution():
    """Katy, Wendi, and Carrie went to a bread-making party. Katy brought three 5-pound bags of flour. Wendi brought twice as much flour as Katy, but Carrie brought 5 pounds less than the amount of flour Wendi brought. How much more flour, in ounces, did Carrie bring than Katy?"""
    katy_flour = 3 * 5 * 16
    wendi_flour = 2 * katy_flour
    carrie_flour = wendi_flour - 5 * 16
    diff = carrie_flour - katy_flour
    result = diff
    return result

print(solution())