def solution():
    # Calculate the total number of galleries and pictures drawn
    total_galleries = 5 + 1  # 5 new galleries + 1 original gallery
    total_pictures = 9 + 5 * x  # each of the 5 new galleries receives x pictures

    # Calculate the total number of pencils used
    total_pencils = 4 * total_pictures + 2 * total_galleries

    # Set up the equation and solve for x
    4 * (9 + 5 * x) + 2 * (5 + 1) = 88
    x = 5

    result = x
    return result

print(solution())