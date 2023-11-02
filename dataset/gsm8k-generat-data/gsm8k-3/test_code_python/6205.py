def solution():
    """Mark realizes that a lot of the friends on his friends list are people he doesn't talk to anymore.  He keeps 40% of his friends list and then contacts the rest.  Of those only 50% respond.  He removes everyone who did not respond.  If he had 100 friends how many does he have left after the removal?"""
    # Define the initial number of friends
    total_friends = 100

    # Calculate the number of friends Mark wants to keep
    friends_to_keep = int(total_friends * 0.4)

    # Calculate the number of friends Mark contacts
    friends_to_contact = total_friends - friends_to_keep

    # Calculate the number of friends who respond
    friends_respond = int(friends_to_contact * 0.5)

    # Calculate the number of friends Mark removes
    friends_to_remove = friends_to_contact - friends_respond

    # Calculate the number of friends Mark has left after the removal
    friends_left = friends_to_keep + friends_respond

    # Display the number of friends Mark has left
    result = friends_left
    return result

print(solution())