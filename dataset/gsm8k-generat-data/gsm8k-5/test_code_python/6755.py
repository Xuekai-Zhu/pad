def solution():
    total_pictures = 9 + 5 * x  # Alexander draws 9 pictures for the first gallery and x pictures for each new gallery
    total_pencils = 88  # Alexander uses 88 pencils in total
    pencils_per_picture = 4  # Alexander needs 4 pencils per picture
    pencils_for_signature = 2  # Alexander needs 2 additional pencils for signing each picture

    # Calculate the total number of pencils used for the pictures
    pencils_for_pictures = pencils_per_picture * total_pictures

    # Calculate the total number of pencils used for signatures
    pencils_for_signatures = pencils_for_signature * total_pictures

    # Calculate the total number of pencils used
    total_pencils_used = pencils_for_pictures + pencils_for_signatures

    # Calculate the number of pictures at each new gallery
    pictures_per_gallery = (total_pictures - 9) // 5

    result = pictures_per_gallery
    return result

print(solution())