def solution():
    """Denny, an Instagram influencer, has 100000 followers and gets 1000 new followers every day. How many followers will he have if 20000 people unfollowed him in a year?"""
    starting_followers = 100000
    daily_follower_increase = 1000
    year_days = 365
    lost_followers = 20000
    final_followers = starting_followers + (daily_follower_increase * year_days) - lost_followers
    result = final_followers
    return result

print(solution())