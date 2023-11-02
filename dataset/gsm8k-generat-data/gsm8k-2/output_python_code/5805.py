def solution():
    """Dylan filled his glass with ice cubes before he poured his soda into it. He counted and there were 8 ice cubes in his glass. Later when he prepares a pitcher of lemonade he puts two times as many ice cubes in the pitcher. Then it is time to refill the ice cube trays which have 12 spaces each for ice cubes. How many trays does Dylan need to fill if he used exactly all the ice they had in them?"""
    glass_ice_cubes = 8
    pitcher_ice_cubes = 2 * glass_ice_cubes
    total_ice_cubes = glass_ice_cubes + pitcher_ice_cubes
    trays_needed = total_ice_cubes // 12 + (total_ice_cubes % 12 > 0)  # Use floor division and modulo to round up if needed
    result = trays_needed
    return result

print(solution())