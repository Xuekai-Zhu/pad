def solution():
    """Denny, an Instagram influencer, has 100000 followers and gets 1000 new followers every day. How many followers will he have if 20000 people unfollowed him in a year?"""
    starting_followers = 100000
    daily_followers = 1000
    lost_followers = 20000
    days_in_year = 365
    final_followers = starting_followers + (daily_followers * days_in_year) - lost_followers
    result = final_followers
    return result

print(solution())