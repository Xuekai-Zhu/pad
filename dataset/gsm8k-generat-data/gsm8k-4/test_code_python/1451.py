def solution():
    """Denny, an Instagram influencer, has 100000 followers and gets 1000 new followers every day. How many followers will he have if 20000 people unfollowed him in a year?"""
    # Define the initial number of followers
    followers = 100000

    # Calculate the number of followers after one year, accounting for 365 days and 20000 unfollows
    followers = followers + (365 * 1000) - 20000

    # Return the result
    result = followers
    return result

print(solution())