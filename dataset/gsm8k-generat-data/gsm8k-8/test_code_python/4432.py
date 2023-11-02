def solution():
    # Calculate the total number of days in January and February
    num_days = 31 + 28

    # Calculate the number of photos Shane took in January
    january_photos = 2 * 31

    # Calculate the number of photos Shane took in February
    february_photos = 146 - january_photos

    # Calculate the number of weeks in February
    num_weeks = (num_days - 31) // 7 + 1

    # Calculate the average number of photos Shane took each week in February
    february_photos_per_week = february_photos / num_weeks

    result = february_photos_per_week
    return result

print(solution())