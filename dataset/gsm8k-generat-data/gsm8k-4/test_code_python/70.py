def solution():
    """Tim has 30 less apples than Martha, and Harry has half as many apples as Tim. If Martha has 68 apples, how many apples does Harry have?"""
    # Define the number of apples Martha has
    martha_apples = 68

    # Calculate the number of apples Tim has (30 less than Martha)
    tim_apples = martha_apples - 30

    # Calculate the number of apples Harry has (half as many as Tim)
    harry_apples = tim_apples / 2

    # return the result
    result = harry_apples
    return result

print(solution())