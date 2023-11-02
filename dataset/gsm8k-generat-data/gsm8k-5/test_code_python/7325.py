def solution():
    john_height = 152  # John's height is given to be 152 cm
    lena_height = john_height - 15  # Lena is 15 cm shorter than John
    rebeca_height = john_height + 6  # Rebeca is 6 cm taller than John

    # Calculate the total height of Lena and Rebeca together
    total_height = lena_height + rebeca_height
    result = total_height
    return result

print(solution())