def solution():
    initial_followers = 100000
    new_followers_per_day = 1000
    num_days_in_year = 365
    num_unfollowers = 20000

    # Calculate the total number of new followers in a year
    total_new_followers = new_followers_per_day * num_days_in_year

    # Calculate the total number of followers after a year
    total_followers = initial_followers + total_new_followers - num_unfollowers
    result = total_followers
    return result

print(solution())