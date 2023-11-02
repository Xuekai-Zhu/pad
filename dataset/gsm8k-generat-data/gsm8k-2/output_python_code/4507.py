def solution():
    """A YouTube video got 3000 likes and 100 more than half as many dislikes. If the video gets 1000 more dislikes and 0 more likes how many dislikes does the video have?"""
    likes = 3000
    dislikes = (likes // 2) + 100
    dislikes += 1000
    result = dislikes
    return result

print(solution())