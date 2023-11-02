def solution():
    # Define the number of friends in classes and after-school clubs
    friends_in_classes = 6
    friends_in_clubs = 0.5 * friends_in_classes

    # Calculate the total number of friends
    total_friends = friends_in_classes + friends_in_clubs

    # Calculate the total inches of thread needed
    total_inches = total_friends * 12

    result = total_inches
    return result

print(solution())