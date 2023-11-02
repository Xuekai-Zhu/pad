def solution():
    """Kennedy's house is 600 square feet larger than 4 times Benedict's house. If Kennedy's house is 10000 square feet, how many square feet is Benedict's house?"""
    # Define Kennedy's house size and the relationship between Kennedy's and Benedict's house sizes
    kennedy_house = 10000
    kennedy_benedict_relationship = 4

    # Calculate Benedict's house size using the relationship to Kennedy's house size
    benedict_house = (kennedy_house - 600) / kennedy_benedict_relationship

    # return the result
    result = benedict_house
    return result

print(solution())