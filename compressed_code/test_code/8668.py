def solution():
    
    insta_followers = 240
    fb_followers = 500
    twitter_followers = (insta_followers + fb_followers) / 2
    tiktok_followers = twitter_followers * 3
    youtube_followers = tiktok_followers + 510
    total_followers = insta_followers + fb_followers + twitter_followers + tiktok_followers + youtube_followers
    result = total_followers
    return result

print(solution())