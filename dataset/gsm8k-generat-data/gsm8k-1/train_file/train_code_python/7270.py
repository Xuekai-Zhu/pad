def solution():
    """Cristina, John, Clarissa and Sarah want to give their mother a photo album for her birthday. Cristina brings 7 photos, John brings 10 photos and Sarah brings 9 photos. If the photo album has 40 slots available, how many photos does Clarissa need to bring in order to complete the photo album?"""
    total_photos_brought = 7 + 10 + 9
    slots_available = 40
    clarissa_photos_needed = slots_available - total_photos_brought
    result = clarissa_photos_needed
    return result

print(solution())