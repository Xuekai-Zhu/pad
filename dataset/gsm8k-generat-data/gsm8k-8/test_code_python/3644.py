def solution():
    # Define the number of followers on each platform
    insta_followers = 240
    fb_followers = 500
    twitter_followers = (insta_followers + fb_followers) / 2
    tiktok_followers = 3 * twitter_followers
    youtube_followers = tiktok_followers + 510

    # Calculate the total number of followers
    total_followers = insta_followers + fb_followers + twitter_followers + tiktok_followers + youtube_followers
    result = total_followers
    return result

print(solution())