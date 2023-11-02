def solution():
    # Define the number of photos each person brings
    cristina_photos = 7
    john_photos = 10
    sarah_photos = 9

    # Calculate the total number of photos already brought
    total_photos = cristina_photos + john_photos + sarah_photos

    # Calculate the number of remaining slots in the photo album
    remaining_slots = 40 - total_photos

    # Clarissa needs to bring the remaining number of photos
    clarissa_photos = remaining_slots
    result = clarissa_photos
    return result

print(solution())