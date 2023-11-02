def solution():
    """Anna wants to plant red and yellow tulips in the shape of a smiley face. She needs 8 red tulips for each eye and 18 red tulips for the smile. If she needs 9 times the number of tulips in the smile to make the yellow background of the face, how many tulips does she need total?"""
    # Define the number of red tulips for each feature
    RED_EYE_TULIPS = 8
    RED_SMILE_TULIPS = 18

    # Calculate the total number of red tulips needed
    red_tulips = 2 * RED_EYE_TULIPS + RED_SMILE_TULIPS

    # Calculate the number of yellow tulips needed for the background
    yellow_tulips = 9 * RED_SMILE_TULIPS

    # Calculate the total number of tulips needed
    total_tulips = red_tulips + yellow_tulips

    # Display the total number of tulips
    result = total_tulips
    return result

print(solution())