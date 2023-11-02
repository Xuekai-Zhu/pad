def solution():
    """Denny, an Instagram influencer, has 100000 followers and gets 1000 new followers every day. How many followers will he have if 20000 people unfollowed him in a year?"""
    # Define the initial number of followers and the number of new followers per day
    initial_followers = 100000
    new_followers_per_day = 1000

    # Calculate the total number of followers after one year
    total_followers = initial_followers + (new_followers_per_day * 365) - 20000

    # Display the total number of followers
    result = total_followers
    return result

print(solution())