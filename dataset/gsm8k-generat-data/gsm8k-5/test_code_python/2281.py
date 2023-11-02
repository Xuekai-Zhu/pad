def solution():
    girls = 3 # Willow's daughter had 3 friends over for a slumber party
    pancakes_serving = 4 # Willow's pancake recipe makes a serving of 4 pancakes
    servings_per_girl = 1.5 # Each girl wanted a serving and a half of pancakes
    pancakes_girls = girls * servings_per_girl # Total pancakes needed by the girls
    pancakes_son = 3 * pancakes_serving # Total pancakes needed by Willow's son

    # Calculate the total number of pancakes needed
    total_pancakes = pancakes_girls + pancakes_son

    result = total_pancakes
    return result

print(solution())