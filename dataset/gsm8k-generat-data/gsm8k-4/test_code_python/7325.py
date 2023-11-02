def solution():
    """John is 15 cm taller than Lena and 6 cm shorter than Rebeca. If John has a height of 152 cm, what is the height of Lena and Rebeca together?"""
    # Define John's height and the height differences between John and Lena/Rebeca
    john_height = 152
    lena_john_height_diff = -15
    john_rebeca_height_diff = 6

    # Calculate Lena's height
    lena_height = john_height + lena_john_height_diff

    # Calculate Rebeca's height
    rebeca_height = john_height + john_rebeca_height_diff

    # Calculate the total height of Lena and Rebeca together
    total_height = lena_height + rebeca_height

    result = total_height
    return result

print(solution())