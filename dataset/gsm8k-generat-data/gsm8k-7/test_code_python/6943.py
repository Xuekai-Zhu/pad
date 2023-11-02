def solution():
    animal_photos = 10
    flower_photos = animal_photos * 3
    scenery_photos = flower_photos - 10

    # Calculate the total number of photos Lisa took last weekend
    total_photos = animal_photos + flower_photos + scenery_photos - 15
    result = total_photos
    return result

print(solution())