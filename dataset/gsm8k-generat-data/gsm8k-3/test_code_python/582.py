def solution():
    """Haruto has tomato plants in his backyard. This year the plants grew 127 tomatoes. Birds had eaten 19 of the tomatoes. He picked the rest. If Haruto gave half of his tomatoes to his friend, how many tomatoes does he have left?"""
    # Define the number of tomatoes that grew and the number eaten by birds
    total_tomatoes = 127
    eaten_tomatoes = 19

    # Calculate the number of tomatoes that Haruto picked
    picked_tomatoes = total_tomatoes - eaten_tomatoes

    # Calculate the number of tomatoes that Haruto gave to his friend
    given_tomatoes = picked_tomatoes // 2

    # Calculate the number of tomatoes that Haruto has left
    remaining_tomatoes = picked_tomatoes - given_tomatoes

    # Display the number of tomatoes that Haruto has left
    result = remaining_tomatoes
    return result

print(solution())