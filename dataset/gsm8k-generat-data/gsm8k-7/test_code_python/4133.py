def solution():
    red_tulips_per_eye = 8
    red_tulips_for_smile = 18
    yellow_tulips_for_smile = 9 * red_tulips_for_smile

    # Calculate the total number of red tulips needed for the smiley face
    total_red_tulips = 2 * red_tulips_per_eye + red_tulips_for_smile

    # Calculate the total number of yellow tulips needed for the smiley face
    total_yellow_tulips = yellow_tulips_for_smile

    # Calculate the total number of tulips needed for the smiley face
    total_tulips = total_red_tulips + total_yellow_tulips
    result = total_tulips
    return result

print(solution())