def solution():
    """Dylan filled his glass with ice cubes before he poured his soda into it. He counted and there were 8 ice cubes in his glass. Later when he prepares a pitcher of lemonade he puts two times as many ice cubes in the pitcher. Then it is time to refill the ice cube trays which have 12 spaces each for ice cubes. How many trays does Dylan need to fill if he used exactly all the ice they had in them?"""
    # Calculate the number of ice cubes in the pitcher
    pitcher_ice_cubes = 8 * 2

    # Calculate the total number of ice cubes needed
    total_ice_cubes = 8 + pitcher_ice_cubes

    # Calculate the number of trays needed to fill with all the ice cubes
    trays_needed = total_ice_cubes // 12

    # Handle the case where there are leftover ice cubes
    if total_ice_cubes % 12 != 0:
        trays_needed += 1

    # Display the number of trays needed
    result = trays_needed
    return result

print(solution())