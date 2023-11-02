def solution():
    stars_required = 85 * 4  # Luke needs to fill 4 bottles with paper stars
    stars_made = 33  # Luke has already made 33 paper stars

    # Calculate the number of stars Luke needs to make
    stars_needed = stars_required - stars_made
    result = stars_needed
    return result

print(solution())