def solution():
    num_exhibitions = 5

    # Calculate the total number of pictures Alexander drew
    total_pictures = 9 + (num_exhibitions * x)

    # Calculate the total number of pencils used for drawing
    pencils_for_drawing = total_pictures * 4

    # Calculate the total number of pencils used for signing
    pencils_for_signing = num_exhibitions * 2

    # Calculate the total number of pencils used
    total_pencils = pencils_for_drawing + pencils_for_signing

    # Solve for x, the number of pictures at each new gallery
    x = (total_pencils - (9 * 4)) / (num_exhibitions * 6)

    result = x
    return result

print(solution())