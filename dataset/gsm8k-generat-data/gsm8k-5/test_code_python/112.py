def solution():
    gallery_photos = 400
    first_day_photos = gallery_photos / 2
    second_day_photos = first_day_photos + 120
    total_photos = gallery_photos + first_day_photos + second_day_photos
    result = total_photos
    return result

print(solution())