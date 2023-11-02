def solution():
    """Jasmine's teacher gives stickers for reward. She was given 15 stickers for participating in class, but she lost 7 stickers during playtime. However, her teacher gave her another 5 stickers for helping her classmates. How many stickers does she have at the end?"""
    initial_stickers = 15
    lost_stickers = 7
    extra_stickers = 5
    total_stickers = initial_stickers - lost_stickers + extra_stickers
    result = total_stickers
    return result

print(solution())