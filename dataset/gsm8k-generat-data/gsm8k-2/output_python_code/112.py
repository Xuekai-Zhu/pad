def solution():
    """Lilah's family gallery has 400 photos. On a two-day trip to the Grand Canyon, they took half as many photos they have in the family's gallery on the first day and 120 more photos than they took on the first day on the second day. If they added all these photos to the family gallery, calculate the total number of photos in the gallery."""
    gallery_photos = 400
    first_day_photos = gallery_photos / 2
    second_day_photos = first_day_photos + 120
    total_photos = gallery_photos + first_day_photos + second_day_photos
    result = total_photos
    return result

print(solution())