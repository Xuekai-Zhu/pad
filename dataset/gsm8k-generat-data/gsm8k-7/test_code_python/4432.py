def solution():
    january_photos = 2 * 31  # January has 31 days
    february_photos = 146 - january_photos

    # Calculate the number of weeks in February
    num_weeks = 4  # February has 4 weeks

    # Calculate the number of photos Shane took each week in February
    photos_per_week = (february_photos - 2) / num_weeks  # Subtract 2 photos already taken in the first week
    result = photos_per_week
    return result

print(solution())