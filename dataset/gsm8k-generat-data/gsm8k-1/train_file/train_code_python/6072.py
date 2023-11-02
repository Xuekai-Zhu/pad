def solution():
    """ Three fifths of the light bulbs in the kitchen are broken. A third of the light bulbs in the foyer are also broken. If 10 light bulbs in the foyer are broken and there are 35 light bulbs in the kitchen, then how many light bulbs are not broken in both the foyer and kitchen? """
    kitchen_broken = 35 * 3/5
    foyer_broken = 10
    kitchen_not_broken = 35 - kitchen_broken
    foyer_not_broken = (foyer_broken * 3) - 10
    total_not_broken = kitchen_not_broken + foyer_not_broken
    result = total_not_broken
    
    return result

print(solution())