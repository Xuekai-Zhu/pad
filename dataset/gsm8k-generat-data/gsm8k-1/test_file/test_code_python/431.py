def solution():
    """Ray had 25 lollipops. He kept 5 lollipops and shared the remaining equally with his four friends. How many lollipops did each of his friends receive?"""
    total_lollipops = 25
    kept_lollipops = 5
    shared_lollipops = total_lollipops - kept_lollipops
    friends = 4
    lollipops_per_friend = shared_lollipops // friends
    result = lollipops_per_friend
    return result

print(solution())