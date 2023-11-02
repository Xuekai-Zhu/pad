def solution():
    day_one_birds = 300
    day_two_birds = day_one_birds * 2
    day_three_birds = day_two_birds - 200

    # Calculate the total number of birds seen in three days
    total_birds_seen = day_one_birds + day_two_birds + day_three_birds
    result = total_birds_seen
    return result

print(solution())