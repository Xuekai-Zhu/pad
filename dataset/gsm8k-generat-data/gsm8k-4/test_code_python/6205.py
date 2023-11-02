def solution():
    """Mark realizes that a lot of the friends on his friends list are people he doesn't talk to anymore. He keeps 40% of his friends list and then contacts the rest. Of those only 50% respond. He removes everyone who did not respond. If he had 100 friends how many does he have left after the removal?"""
    # Define the initial number of friends
    initial_friends = 100

    # Calculate the number of friends he keeps
    keep_friends = int(initial_friends * 0.4)

    # Calculate the number of friends he contacts
    contact_friends = initial_friends - keep_friends

    # Calculate the number of friends who respond
    respond_friends = int(contact_friends * 0.5)

    # Calculate the number of friends he removes
    remove_friends = contact_friends - respond_friends

    # Calculate the final number of friends
    final_friends = keep_friends + respond_friends

    # return the final number of friends
    result = final_friends
    return result

print(solution())