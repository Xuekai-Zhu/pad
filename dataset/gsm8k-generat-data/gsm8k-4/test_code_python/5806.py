def solution():
    """Dylan filled his glass with ice cubes before he poured his soda into it. He counted and there were 8 ice cubes in his glass. Later when he prepares a pitcher of lemonade he puts two times as many ice cubes in the pitcher. Then it is time to refill the ice cube trays which have 12 spaces each for ice cubes. How many trays does Dylan need to fill if he used exactly all the ice they had in them?"""
    # Calculate the total number of ice cubes used in the pitcher of lemonade
    lemonade_cubes = 8 * 2

    # Calculate the total number of ice cubes used in the glass and the pitcher
    total_cubes = 8 + lemonade_cubes

    # Calculate the number of ice cube trays needed to refill all the used ice cubes
    trays_needed = total_cubes // 12

    if total_cubes % 12 != 0:
        trays_needed += 1

    result = trays_needed
    return result

print(solution())