def solution():
    first_two_months = 146  # Shane took 146 photos in the first 2 months
    january_photos = 2 * 31  # Shane took 2 photos every day in January
    february_photos = first_two_months - january_photos  # Subtract January photos to get February photos
    weeks_in_february = 4  # There are 4 weeks in February

    # Calculate the number of photos Shane took each week in February
    photos_per_week = february_photos / weeks_in_february
    result = photos_per_week
    return result

print(solution())