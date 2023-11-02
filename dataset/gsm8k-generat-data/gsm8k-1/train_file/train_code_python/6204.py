def solution():
    """Mark realizes that a lot of the friends on his friends list are people he doesn't talk to anymore. He keeps 40% of his friends list and then contacts the rest. Of those only 50% respond. He removes everyone who did not respond. If he had 100 friends how many does he have left after the removal?"""
    initial_friends = 100
    percent_kept = 40
    percent_contacted = 60
    percent_responded = 50
    friends_kept = initial_friends * (percent_kept / 100)
    friends_contacted = initial_friends - friends_kept
    friends_responded = friends_contacted * (percent_responded / 100)
    friends_left = friends_kept + friends_responded
    result = friends_left
    return result

print(solution())