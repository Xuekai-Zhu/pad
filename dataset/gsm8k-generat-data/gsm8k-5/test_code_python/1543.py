def solution():
    ken_situps = 20  # Ken can do 20 sit-ups
    nathan_situps = ken_situps * 2  # Nathan can do twice as many sit-ups as Ken
    combined_situps = ken_situps + nathan_situps  # The combined sit-ups of Ken and Nathan
    bob_situps = combined_situps / 2  # Bob can do half the number of Ken and Nathan's combined sit-ups

    # Calculate the difference between Bob's and Ken's sit-ups
    difference = bob_situps - ken_situps
    result = difference
    return result

print(solution())