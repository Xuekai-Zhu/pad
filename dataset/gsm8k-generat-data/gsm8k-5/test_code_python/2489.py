def solution():
    samara_alligators = 20  # Samara saw 20 alligators
    friends_alligators = 10  # Each of Samara's friends saw 10 alligators on average
    total_friends = 3  # Samara had three friends with her on the search

    # Calculate the total number of alligators seen by Samara and her friends
    total_alligators = samara_alligators + (friends_alligators * total_friends)
    result = total_alligators
    return result

print(solution())