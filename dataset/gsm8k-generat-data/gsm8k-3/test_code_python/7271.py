def solution():
    """Cristina, John, Clarissa and Sarah want to give their mother a photo album for her birthday. Cristina brings 7 photos, John brings 10 photos and Sarah brings 9 photos. If the photo album has 40 slots available, how many photos does Clarissa need to bring in order to complete the photo album?"""
    # Calculate the total number of photos brought by Cristina, John and Sarah
    total_photos = 7 + 10 + 9

    # Calculate the number of photos Clarissa needs to bring
    clarissa_photos = 40 - total_photos

    # Display the number of photos Clarissa needs to bring
    result = clarissa_photos
    return result

print(solution())