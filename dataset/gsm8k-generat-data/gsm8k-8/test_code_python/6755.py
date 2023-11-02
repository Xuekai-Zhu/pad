def solution():
    # Define the given values
    total_pictures = 9 + 5 * x  # where x is the number of pictures at each new gallery
    pencils_per_picture = 4
    pencils_for_signature = 2

    # Calculate the total pencils used
    total_pencils = pencils_per_picture * total_pictures + pencils_for_signature * 5

    # Find the number of pictures at each new gallery
    x = (total_pencils - pencils_for_signature * 5) / (pencils_per_picture * 5)

    result = x
    return result

print(solution())