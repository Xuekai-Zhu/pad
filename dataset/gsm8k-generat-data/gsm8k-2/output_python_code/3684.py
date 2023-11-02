def solution():
    """85 paper stars are required to fill a glass jar. Luke has already made 33 stars, but he needs to fill 4 bottles. How many more stars must Luke make?"""
    total_paper_stars = 85 * 4
    already_made_stars = 33
    remaining_stars = total_paper_stars - already_made_stars
    result = remaining_stars
    return result

print(solution())