def solution():
    """Larry and Barry want to pick apples out of the tree, but neither is tall enough to reach the apples. Barry can reach apples that are 5 feet high. Larry is 5 feet tall, but his shoulder height is 20% less than his full height. If Barry stands on Larry's shoulders, how high can they reach?"""
    barry_reach = 5
    larry_height = 5
    larry_shoulder_height = larry_height - (larry_height * 0.2)
    combined_reach = barry_reach + larry_shoulder_height
    result = combined_reach
    return result

print(solution())