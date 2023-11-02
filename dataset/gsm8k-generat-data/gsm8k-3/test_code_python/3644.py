def solution():
    """Malcolm has 240 followers on Instagram and 500 followers on Facebook. The number of followers he has on Twitter is half the number of followers he has on Instagram and Facebook combined. Meanwhile, the number of followers he has on TikTok is 3 times the number of followers is has on Twitter, and he has 510 more followers on Youtube than he has on TikTok. How many followers does Malcolm have on all his social media?"""
    # Define the number of followers on each platform
    instagram_followers = 240
    facebook_followers = 500
    twitter_followers = (instagram_followers + facebook_followers) / 2
    tiktok_followers = 3 * twitter_followers
    youtube_followers = tiktok_followers + 510

    # Calculate the total number of followers
    total_followers = instagram_followers + facebook_followers + twitter_followers + tiktok_followers + youtube_followers

    # Display the total number of followers
    result = total_followers
    return result

print(solution())