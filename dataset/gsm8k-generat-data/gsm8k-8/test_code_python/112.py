def solution():
    # Define total number of photos in family gallery
    family_gallery = 400

    # Calculate number of photos taken on first day
    day1_photos = family_gallery / 2

    # Calculate number of photos taken on second day
    day2_photos = day1_photos + 120

    # Calculate total number of photos after the trip
    total_photos = family_gallery + day1_photos + day2_photos
    result = total_photos
    return result

print(solution())