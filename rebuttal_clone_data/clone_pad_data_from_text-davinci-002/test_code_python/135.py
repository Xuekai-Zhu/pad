def solution():
    """Kennedy's house is 600 square feet larger than 4 times Benedict's house. If Kennedy's house is 10000 square feet, how many square feet is Benedict's house?"""
    kennedy_house = 10000
    difference = 600
    benedict_house = kennedy_house - (4 * difference)
    result = benedict_house
    return result

print(solution())