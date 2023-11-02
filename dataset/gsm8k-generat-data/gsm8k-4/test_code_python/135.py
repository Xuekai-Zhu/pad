def solution():
    """Kennedy's house is 600 square feet larger than 4 times Benedict's house. If Kennedy's house is 10000 square feet, how many square feet is Benedict's house?"""
    # Define Kennedy's house size and the size ratio between Kennedy's and Benedict's houses
    kennedy_size = 10000
    ratio = 4

    # Calculate the size of Benedict's house
    benedict_size = (kennedy_size - 600) / ratio

    # Return the result
    result = benedict_size
    return result

print(solution())