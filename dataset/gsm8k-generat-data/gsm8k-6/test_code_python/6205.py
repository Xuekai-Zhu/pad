def solution():
    # Calculate the number of friends Mark keeps
    remaining_friends = 0.4 * 100  

    # Calculate the number of friends who don't respond
    non_responders = 0.6 * 100  # Mark contacts the remaining 60% of his friends list
    no_response = 0.5 * non_responders  

    # Calculate the number of friends left after removing non-responders
    friends_left = remaining_friends - no_response
    result = friends_left
    return result

print(solution())