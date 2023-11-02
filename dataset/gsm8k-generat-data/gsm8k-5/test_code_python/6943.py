def solution():
    animal_photos = 10
    flower_photos = 3 * animal_photos
    scenery_photos = flower_photos - 10
    total_photos = animal_photos + flower_photos + scenery_photos  # Total number of photos taken by Leslie

    last_weekend_photos = total_photos - 15  # Total number of photos taken by Lisa last weekend

    result = last_weekend_photos
    return result

print(solution())