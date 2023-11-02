def solution():
    followers = 100000
    new_followers_per_day = 1000
    days_in_a_year = 365
    unfollowed_per_year = 20000
    followers_gained = new_followers_per_day * days_in_a_year
    total_followers = followers + followers_gained - unfollowed_per_year
    result = total_followers
    return result

print(solution())