def solution():
    """Mark realizes that a lot of the friends on his friends list are people he doesn't talk to anymore. He keeps 40% of his friends list and then contacts the rest. Of those only 50% respond. He removes everyone who did not respond. If he had 100 friends how many does he have left after the removal?"""
    total_friends = 100
    keep_friends_percentage = 0.4
    contacted_friends = total_friends - int(total_friends * keep_friends_percentage)
    responded_percentage = 0.5
    non_responded_friends = contacted_friends - int(contacted_friends * responded_percentage)
    friends_left = total_friends - non_responded_friends
    result = friends_left
    return result

print(solution())