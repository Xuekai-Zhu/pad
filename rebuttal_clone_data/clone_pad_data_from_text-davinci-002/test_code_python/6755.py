def solution():
    pencils_for_painting = 4
    pencils_for_signing = 2
    total_pencils_used = 88
    total_pictures = total_pencils_used / (pencils_for_painting + pencils_for_signing)
    pictures_per_gallery = total_pictures / 5
    result = pictures_per_gallery
    return result

print(solution())