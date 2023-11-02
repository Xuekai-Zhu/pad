def solution():
    sitting_time = 6 * 60  # Gretchen spends 6 hours working at her desk
    walking_time = sitting_time // 90 * 10  # Gretchen should spend 10 minutes walking for every 90 minutes sitting

    # Convert walking time from minutes to hours and minutes
    walking_hours = walking_time // 60
    walking_minutes = walking_time % 60

    # Format the result as a string in "hours:minutes" format
    result = f"{walking_hours}:{walking_minutes:02}"
    return result

print(solution())