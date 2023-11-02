def solution():
    """Anna wants to plant red and yellow tulips in the shape of a smiley face. She needs 8 red tulips for each eye and 18 red tulips for the smile. If she needs 9 times the number of tulips in the smile to make the yellow background of the face, how many tulips does she need total?"""
    # Define the number of tulips needed for each part of the smiley face
    red_eyes = 2 * 8
    red_smile = 18
    yellow_background = 9 * red_smile

    # Calculate the total number of tulips needed
    total_tulips = red_eyes + red_smile + yellow_background

    # return the result
    result = total_tulips
    return result

print(solution())