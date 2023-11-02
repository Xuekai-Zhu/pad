def solution():
    
    starting_followers = 100000
    daily_follower_increase = 1000
    year_days = 365
    lost_followers = 20000
    final_followers = starting_followers + (daily_follower_increase * year_days) - lost_followers
    result = final_followers
    return result

print(solution())