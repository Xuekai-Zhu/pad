def solution():
    
    instagram_followers = 240
    facebook_followers = 500
    twitter_followers = (instagram_followers + facebook_followers) / 2
    tiktok_followers = 3 * twitter_followers
    youtube_followers = tiktok_followers + 510
    total_followers = instagram_followers + facebook_followers + twitter_followers + tiktok_followers + youtube_followers
    result = total_followers
    return result

print(solution())