def solution():
    """Ezekiel hikes as a hobby. This past summer, he did a challenging three-day hike across 50 kilometers of wilderness. The first day, he covered 10 kilometers of steep mountainside. The second day was flatter and he was able to cover half the full hike distance. How many kilometers did he have to hike on the third day to finish the hike?"""
    # Define the total hike distance in kilometers
    total_distance = 50

    # Define the distance covered on the first day
    day1_distance = 10

    # Define the distance covered on the second day
    day2_distance = total_distance / 2 - day1_distance

    # Define the distance remaining on the third day
    day3_distance = total_distance - day1_distance - day2_distance

    # Display the distance remaining on the third day
    result = day3_distance
    return result

print(solution())