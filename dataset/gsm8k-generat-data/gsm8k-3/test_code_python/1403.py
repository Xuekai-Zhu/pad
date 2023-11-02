def solution():
    """Brad’s zip code consists of five numbers that add up to 10. The first and second numbers are the same. The third number is zero. The fourth number is double the first number. The fourth and fifth numbers add up to 8. What is Brad’s zip code?"""
    # We know that the five numbers add up to 10, so:
    # a + a + 0 + b + c = 10
    # 2a + b + c = 10

    # We also know that the fourth number is double the first number:
    # b = 2a

    # And we know that the fourth and fifth numbers add up to 8:
    # b + c = 8

    # Substituting b in the third equation:
    # 2a + c = 8

    # We have two equations with two variables:
    # 2a + b + c = 10
    # 2a + c = 8

    # Subtracting the second equation from the first:
    # b = 2

    # Substituting b in the second equation:
    # a = 1

    # Substituting a and b in the fourth equation:
    # c = 6

    # So Brad’s zip code is 11026
    result = 11026
    return result

print(solution())