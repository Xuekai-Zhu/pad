def solution():
    # Calculate the total number of followers after one year
    starting_followers = 100000
    new_followers_per_day = 1000
    days_in_a_year = 365
    unfollowers_in_a_year = 20000
    total_new_followers = new_followers_per_day * days_in_a_year
    total_followers = starting_followers + total_new_followers - unfollowers_in_a_year
    result = total_followers
    return result

print(solution())