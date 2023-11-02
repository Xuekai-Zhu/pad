def solution():
    """Haruto has tomato plants in his backyard. This year the plants grew 127 tomatoes. Birds had eaten 19 of the tomatoes. He picked the rest. If Haruto gave half of his tomatoes to his friend, how many tomatoes does he have left?"""
    # Define the total number of tomatoes and the number of tomatoes eaten by birds
    total_tomatoes = 127
    bird_eaten_tomatoes = 19

    # Calculate the number of picked tomatoes
    picked_tomatoes = total_tomatoes - bird_eaten_tomatoes

    # Calculate the number of tomatoes given to his friend
    friend_tomatoes = picked_tomatoes / 2

    # Calculate the number of tomatoes left
    tomatoes_left = picked_tomatoes - friend_tomatoes

    result = tomatoes_left
    return result

print(solution())