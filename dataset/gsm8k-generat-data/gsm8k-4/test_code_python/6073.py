def solution():
    """Three fifths of the light bulbs in the kitchen are broken. A third of the light bulbs in the foyer are also broken. If 10 light bulbs in the foyer are broken and there are 35 light bulbs in the kitchen, then how many light bulbs are not broken in both the foyer and kitchen?"""
    # Define the total number of light bulbs in the kitchen
    kitchen_bulbs_total = 35

    # Calculate the number of broken light bulbs in the kitchen
    kitchen_bulbs_broken = (3/5) * kitchen_bulbs_total

    # Calculate the number of working light bulbs in the kitchen
    kitchen_bulbs_working = kitchen_bulbs_total - kitchen_bulbs_broken

    # Define the total number of light bulbs in the foyer
    foyer_bulbs_total = None

    # Calculate the number of broken and working light bulbs in the foyer using the given ratio
    foyer_bulbs_broken = 10
    foyer_bulbs_working = (1-1/3) * foyer_bulbs_broken

    # Calculate the number of light bulbs not broken in both the foyer and kitchen
    bulbs_not_broken = kitchen_bulbs_working + foyer_bulbs_working

    result = bulbs_not_broken
    return result

print(solution())