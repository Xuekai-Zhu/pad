def solution():
    # Calculate the total number of donuts needed for one friend
    donuts_per_friend = 3 + 1

    # Calculate the total number of friends
    total_friends = 5

    # Calculate the total number of donuts needed
    total_donuts = total_friends * donuts_per_friend

    # Add one more donut for Andrew
    total_donuts += 1

    result = total_donuts
    return result

print(solution())