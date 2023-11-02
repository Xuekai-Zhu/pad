def solution():
    """Lilah's family gallery has 400 photos. On a two-day trip to the Grand Canyon, they took half as many photos they have in the family's gallery on the first day and 120 more photos than they took on the first day on the second day. If they added all these photos to the family gallery, calculate the total number of photos in the gallery."""
    photos_in_gallery = 400
    photos_first_day = photos_in_gallery / 2
    photos_second_day = photos_first_day + 120
    total_photos = photos_in_gallery + photos_first_day + photos_second_day
    result = total_photos
    return result

print(solution())