def solution():
    """Ezekiel hikes as a hobby. This past summer, he did a challenging three-day hike across 50 kilometers of wilderness. The first day, he covered 10 kilometers of steep mountainside. The second day was flatter and he was able to cover half the full hike distance. How many kilometers did he have to hike on the third day to finish the hike?"""
    # Define the total hike distance and the first two day's distance
    total_distance = 50
    first_two_days = 10 + (total_distance / 2)

    # Calculate the remaining distance to be covered on the third day
    third_day_distance = total_distance - first_two_days

    result = third_day_distance
    return result

print(solution())