def solution():
    """
    Palmer loves taking photos and has an album of 100 photos under her bed to mark memories of places she's been.
    She recently went on a long trip to Bali.
    Palmer took 50 new pictures in the first week and twice that many in the second week.
    She was running out of space at the end of her trip and took only 80 new photos total across the third and fourth weeks.
    If she adds the pictures from Bali to her collection, how many total photos does Palmer have under her bed now?
    """
    initial_photos = 100
    first_week_photos = 50
    second_week_photos = 2 * first_week_photos
    third_fourth_photos = 80
    total_photos = initial_photos + first_week_photos + second_week_photos + third_fourth_photos
    result = total_photos
    
    return result

print(solution())