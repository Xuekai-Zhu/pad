def solution():
    
    starting_followers = 100000
    daily_followers = 1000
    lost_followers = 20000
    days_in_year = 365
    final_followers = starting_followers + (daily_followers * days_in_year) - lost_followers
    result = final_followers
    return result

print(solution())