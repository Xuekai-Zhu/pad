def solution():
    # Calculate the total number of stars needed
    total_stars = 85 * 4  # 85 stars required to fill one glass jar, and there are 4 bottles to fill
    # Calculate the number of stars Luke already made
    made_stars = 33
    # Calculate the number of stars Luke still needs to make
    remaining_stars = total_stars - made_stars
    result = remaining_stars
    return result

print(solution())