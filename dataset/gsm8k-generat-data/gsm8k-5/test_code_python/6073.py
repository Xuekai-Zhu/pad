def solution():
    # Calculate the number of broken light bulbs in the kitchen
    broken_kitchen = (3/5) * 35

    # Calculate the total number of light bulbs in the foyer
    total_foyer = 10 / (1/3)

    # Calculate the number of broken light bulbs in the foyer
    broken_foyer = 10

    # Calculate the number of light bulbs not broken in both the foyer and kitchen
    not_broken = (35 - broken_kitchen) + (total_foyer - broken_foyer) - (35 + total_foyer - broken_kitchen - broken_foyer)

    result = not_broken
    return result

print(solution())