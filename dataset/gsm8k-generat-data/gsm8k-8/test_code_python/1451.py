def solution():
    start_followers = 100000
    daily_increase = 1000
    days_in_year = 365
    lost_followers = 20000

    # Calculate the total number of new followers gained in a year 
    new_followers = daily_increase * days_in_year

    # Calculate the total number of followers after a year 
    total_followers = start_followers + new_followers - lost_followers
    result = total_followers
    return result

print(solution())