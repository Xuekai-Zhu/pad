def solution():
    """Three fifths of the light bulbs in the kitchen are broken. A third of the light bulbs in the foyer are also broken. If 10 light bulbs in the foyer are broken and there are 35 light bulbs in the kitchen, then how many light bulbs are not broken in both the foyer and kitchen?"""
    # Calculate the number of broken light bulbs in the kitchen
    kitchen_broken = 3/5 * 35

    # Calculate the number of broken light bulbs in the foyer
    foyer_broken = 10

    # Calculate the number of non-broken light bulbs in the kitchen
    kitchen_working = 35 - kitchen_broken

    # Calculate the total number of light bulbs in the foyer
    total_foyer = foyer_broken * 3

    # Calculate the number of non-broken light bulbs in the foyer
    foyer_working = total_foyer - foyer_broken

    # Calculate the number of light bulbs not broken in both the kitchen and foyer
    not_broken = kitchen_working + foyer_working

    # Display the result
    result = not_broken
    return result

print(solution())