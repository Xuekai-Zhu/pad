def solution():
    # Calculate the total number of photos Lisa took
    animal_photos = 10  # Leslie took 10 photos of animals
    flower_photos = 3 * animal_photos  # Leslie took 3 times as many photos of flowers as animals
    scenery_photos = flower_photos - 10  # Leslie took 10 fewer scenery photos than flowers
    total_photos = animal_photos + flower_photos + scenery_photos  # total number of photos Leslie took

    # Calculate the number of photos Lisa took last weekend
    Lisa_photos = total_photos - 15
    result = Lisa_photos
    return result

print(solution())