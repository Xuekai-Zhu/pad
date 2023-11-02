def solution():
    """Cristina, John, Clarissa and Sarah want to give their mother a photo album for her birthday. Cristina brings 7 photos, John brings 10 photos and Sarah brings 9 photos. If the photo album has 40 slots available, how many photos does Clarissa need to bring in order to complete the photo album?"""
    total_photos = 7 + 10 + 9
    album_slots = 40
    clarissa_photos = album_slots - total_photos
    result = clarissa_photos
    return result

print(solution())