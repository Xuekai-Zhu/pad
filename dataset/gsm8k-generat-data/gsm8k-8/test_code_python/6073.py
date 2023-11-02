def solution():
    # Calculate the number of broken light bulbs in the kitchen
    kitchen_broken = 3/5 * 35

    # Calculate the number of working light bulbs in the kitchen
    kitchen_working = 35 - kitchen_broken

    # Calculate the number of broken light bulbs in the foyer
    foyer_broken = 10

    # Calculate the total number of light bulbs in the foyer
    total_foyer = foyer_broken / (1/3)

    # Calculate the number of working light bulbs in the foyer
    foyer_working = total_foyer - foyer_broken

    # Calculate the number of light bulbs not broken in either room
    not_broken = kitchen_working + foyer_working
    result = not_broken
    return result

print(solution())