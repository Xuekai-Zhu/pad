def solution():
    """Dylan filled his glass with ice cubes before he poured his soda into it. He counted and there were 8 ice cubes in his glass. Later when he prepares a pitcher of lemonade he puts two times as many ice cubes in the pitcher. Then it is time to refill the ice cube trays which have 12 spaces each for ice cubes.
    How many trays does Dylan need to fill if he used exactly all the ice they had in them?"""
    ice_cubes_in_glass = 8
    ice_cubes_in_pitcher = 2 * ice_cubes_in_glass
    total_ice_cubes = ice_cubes_in_glass + ice_cubes_in_pitcher
    trays_needed = total_ice_cubes // 12
    if total_ice_cubes % 12 != 0:
        trays_needed += 1
    result = trays_needed
    return result

print(solution())