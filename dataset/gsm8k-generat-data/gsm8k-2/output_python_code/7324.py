def solution():
    """John is 15 cm taller than Lena and 6 cm shorter than Rebeca. If John has a height of 152 cm, what is the height of Lena and Rebeca together?"""
    john_height = 152
    lena_height = john_height - 15
    rebeca_height = john_height + 6
    total_height = lena_height + rebeca_height
    result = total_height
    return result

print(solution())