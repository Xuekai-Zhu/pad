def solution():
    # Calculate the total amount of feed needed for the day
    total_feed = 3 * 3  # Wendi feeds three cups of chicken feed in three separate meals
    morning_feed = 15  # Wendi gives her chickens 15 cups of feed in the morning
    afternoon_feed = 25  # Wendi gives her chickens 25 cups of feed in the afternoon
    remaining_feed = total_feed - morning_feed - afternoon_feed
    result = remaining_feed
    return result

print(solution())