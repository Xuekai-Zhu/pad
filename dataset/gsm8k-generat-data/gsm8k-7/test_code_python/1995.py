def solution():
    initial_photos = 100
    new_photos = 300
    reduction_percentage = 0.20  # 20% reduction

    # Calculate the number of photos that will be taken today
    remaining_percentage = 1 - reduction_percentage
    target_photos = new_photos * remaining_percentage
    photos_to_take = target_photos - initial_photos
    result = photos_to_take
    return result

print(solution())