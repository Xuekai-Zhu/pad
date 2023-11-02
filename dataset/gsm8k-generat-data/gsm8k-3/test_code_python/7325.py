def solution():
    """John is 15 cm taller than Lena and 6 cm shorter than Rebeca. If John has a height of 152 cm, what is the height of Lena and Rebeca together?"""
    # John's height is 152 cm
    john_height = 152

    # Lena is 15 cm shorter than John
    lena_height = john_height - 15

    # Rebecca is 6 cm taller than John
    rebecca_height = john_height + 6

    # Calculate the total height of Lena and Rebecca together
    total_height = lena_height + rebecca_height

    # Display the total height
    result = total_height
    return result

print(solution())