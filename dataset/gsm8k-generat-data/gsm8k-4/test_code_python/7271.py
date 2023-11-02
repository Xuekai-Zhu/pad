def solution():
    """Cristina, John, Clarissa and Sarah want to give their mother a photo album for her birthday. Cristina brings 7 photos, John brings 10 photos and Sarah brings 9 photos. If the photo album has 40 slots available, how many photos does Clarissa need to bring in order to complete the photo album?"""
    # Define the number of slots in the photo album
    album_slots = 40

    # Calculate the total number of photos brought by Cristina, John and Sarah
    total_photos = 7 + 10 + 9

    # Calculate the number of empty slots in the album
    empty_slots = album_slots - total_photos

    # Clarissa needs to bring enough photos to fill the empty slots
    result = empty_slots
    return result

print(solution())