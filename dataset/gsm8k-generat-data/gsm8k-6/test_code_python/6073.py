def solution():
    # Calculate the number of broken light bulbs in the kitchen and foyer
    broken_kitchen = (3/5) * 35
    broken_foyer = 10 / (1/3)

    # Calculate the total number of broken light bulbs
    total_broken = broken_kitchen + broken_foyer

    # Calculate the total number of light bulbs in both kitchen and foyer
    total_bulbs = 35 + (10 / (1/2))

    # Calculate the number of light bulbs that are not broken in both kitchen and foyer
    not_broken = total_bulbs - total_broken

    result = not_broken
    return result

print(solution())