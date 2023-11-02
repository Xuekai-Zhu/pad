def solution():
    """85 paper stars are required to fill a glass jar. Luke has already made 33 stars, but he needs to fill 4 bottles. How many more stars must Luke make?"""
    # Define the total number of stars needed
    TOTAL_STARS = 85 * 4

    # Define the number of stars Luke has already made
    MADE_STARS = 33

    # Calculate the number of stars Luke needs to make
    needed_stars = TOTAL_STARS - MADE_STARS

    # Display the number of stars Luke needs to make
    result = needed_stars
    return result

print(solution())