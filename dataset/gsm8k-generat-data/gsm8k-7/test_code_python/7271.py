def solution():
    cristina_photos = 7
    john_photos = 10
    sarah_photos = 9
    total_photos = cristina_photos + john_photos + sarah_photos
    album_slots = 40

    # Calculate the number of photos Clarissa needs to bring
    clarissa_photos = album_slots - total_photos
    result = clarissa_photos
    return result

print(solution())