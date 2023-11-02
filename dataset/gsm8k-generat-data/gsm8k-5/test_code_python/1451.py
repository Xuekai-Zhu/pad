def solution():
    base_followers = 100000  # Denny starts with 100000 followers
    daily_followers = 1000  # Denny gets 1000 new followers every day
    days_in_year = 365  # There are 365 days in a year
    lost_followers = 20000  # 20000 people unfollowed Denny in a year

    # Calculate the total number of followers Denny will have after a year
    total_followers = (base_followers + (daily_followers * days_in_year)) - lost_followers
    result = total_followers
    return result

print(solution())