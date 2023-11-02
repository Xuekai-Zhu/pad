def solution():
    num_friends = 3
    pancakes_per_serving = 4
    servings_per_person = 1.5
    son_servings = 3

    # Calculate the total number of servings of pancakes needed for the friends
    total_friend_servings = num_friends * servings_per_person

    # Calculate the total number of servings of pancakes needed for everyone
    total_servings = total_friend_servings + son_servings

    # Calculate the total number of pancakes needed
    total_pancakes = total_servings * pancakes_per_serving

    result = total_pancakes
    return result

print(solution())