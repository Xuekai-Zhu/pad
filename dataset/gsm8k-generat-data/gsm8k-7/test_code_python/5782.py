def solution():
    old_album = 100
    week_one_photos = 50
    week_two_photos = 2 * week_one_photos
    week_three_photos = 40
    week_four_photos = 80 - week_three_photos

    # Calculate the total number of new photos from Bali
    total_new_photos = week_one_photos + week_two_photos + week_three_photos + week_four_photos

    # Calculate the new total number of photos in Palmer's album
    new_total_photos = old_album + total_new_photos
    result = new_total_photos
    return result

print(solution())