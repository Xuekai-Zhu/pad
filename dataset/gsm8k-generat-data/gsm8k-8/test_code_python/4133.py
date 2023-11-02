def solution():
    # Calculate the number of red tulips needed for both eyes
    red_tulips_eyes = 2 * 8

    # Calculate the number of red tulips needed for the smile
    red_tulips_smile = 18

    # Calculate the total number of red tulips needed
    total_red_tulips = red_tulips_eyes + red_tulips_smile

    # Calculate the number of yellow tulips needed for the smiley face
    yellow_tulips_smile = 9 * red_tulips_smile

    # Calculate the total number of tulips needed
    total_tulips = total_red_tulips + yellow_tulips_smile

    result = total_tulips
    return result

print(solution())