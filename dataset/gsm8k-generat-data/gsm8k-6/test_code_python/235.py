def solution():
    # Calculate the total number of model trains Max receives over 5 years
    total_trains = (1 * 5) + (2 * 2 * 5)  # Max gets 1 train for his birthday and 2 trains for each Christmas, over the course of 5 years
    total_trains_after_gift = total_trains * 2  # Max's parents give him double the number of trains he already has
    result = total_trains_after_gift
    return result

print(solution())