def solution():
    """85 paper stars are required to fill a glass jar. Luke has already made 33 stars, but he needs to fill 4 bottles. How many more stars must Luke make?"""
    # Define the total number of paper stars needed
    total_stars_needed = 85 * 4

    # Define the number of paper stars Luke has already made
    stars_made = 33

    # Calculate the number of paper stars Luke still needs to make
    stars_needed = total_stars_needed - stars_made

    # Return the result
    result = stars_needed
    return result

print(solution())