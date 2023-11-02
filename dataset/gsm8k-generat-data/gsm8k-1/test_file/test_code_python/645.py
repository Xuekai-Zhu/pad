def solution():
    """Fishio posted her selfie on Instagram. She received 2000 likes on the photo after 1 week. Three weeks later, the number of likes was 70 times as many as the initial number of likes. If she received 20000 more new likes recently, how many Instagram likes are there?"""
    initial_likes = 2000
    likes_three_weeks_later = initial_likes * 70
    total_likes = likes_three_weeks_later + initial_likes + 20000
    result = total_likes
    return result

print(solution())