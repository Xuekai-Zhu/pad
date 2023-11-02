def solution():
    """Palmer loves taking photos and has an album of 100 photos under her bed to mark memories of places she's been. She recently went on a long trip to Bali. Palmer took 50 new pictures in the first week and twice that many in the second week. She was running out of space at the end of her trip and took only 80 new photos total across the third and fourth weeks. If she adds the pictures from Bali to her collection, how many total photos does Palmer have under her bed now?"""
    # Define the number of photos in Palmer's album before the trip
    album_photos = 100

    # Calculate the number of photos Palmer took in the first week
    week1_photos = 50

    # Calculate the number of photos Palmer took in the second week
    week2_photos = week1_photos * 2

    # Calculate the number of photos Palmer took in the third and fourth weeks
    week3_4_photos = 80

    # Calculate the total number of photos Palmer took on the trip
    trip_photos = week1_photos + week2_photos + week3_4_photos

    # Calculate the total number of photos Palmer has now
    total_photos = album_photos + trip_photos

    # Display the total number of photos
    result = total_photos
    return result

print(solution())