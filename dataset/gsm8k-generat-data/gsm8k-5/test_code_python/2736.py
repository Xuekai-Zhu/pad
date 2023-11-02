def solution():
    apartment_story = 5  # Paul lives in a 5th story apartment
    trips_per_day = 3  # Paul makes 3 trips out and back each day
    days_per_week = 7  # There are 7 days in a week
    story_height = 10  # Each story is 10 feet tall

    # Calculate the total distance Paul travels vertically in a week
    total_distance = (apartment_story * 2 * story_height * trips_per_day) * days_per_week

    result = total_distance
    return result

print(solution())