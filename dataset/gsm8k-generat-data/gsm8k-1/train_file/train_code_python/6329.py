def solution():
    """Ezekiel hikes as a hobby. This past summer, he did a challenging three-day hike across 50 kilometers of wilderness. The first day, he covered 10 kilometers of steep mountainside. The second day was flatter and he was able to cover half the full hike distance. How many kilometers did he have to hike on the third day to finish the hike?"""
    total_distance = 50
    distance_covered_first_day = 10
    distance_covered_second_day = total_distance / 2
    distance_remaining = total_distance - distance_covered_first_day - distance_covered_second_day
    result = distance_remaining
    return result

print(solution())