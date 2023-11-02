def solution():
    """Three fifths of the light bulbs in the kitchen are broken. A third of the light bulbs in the foyer are also broken. If 10 light bulbs in the foyer are broken and there are 35 light bulbs in the kitchen,
    then how many light bulbs are not broken in both the foyer and kitchen?"""
    kitchen_broken = 3/5 * 35
    kitchen_not_broken = 35 - kitchen_broken
    foyer_broken = 10
    foyer_not_broken = (2/3) * (kitchen_not_broken + kitchen_broken) - foyer_broken
    result = kitchen_not_broken + foyer_not_broken
    return result

print(solution())