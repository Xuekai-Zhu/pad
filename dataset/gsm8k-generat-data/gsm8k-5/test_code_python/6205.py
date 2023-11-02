def solution():
    total_friends = 100  # Mark has 100 friends on his list
    retained_friends = total_friends * 0.4  # Mark wants to keep 40% of his friends
    contacted_friends = total_friends - retained_friends  # Mark contacts the remaining 60% of his friends
    responded_friends = contacted_friends * 0.5  # Only 50% of the contacted friends respond

    # Calculate the total number of friends Mark has left after the removal
    total_left = retained_friends + responded_friends
    result = total_left
    return result

print(solution())