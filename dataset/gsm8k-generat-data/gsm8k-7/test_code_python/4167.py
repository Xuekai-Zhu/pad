def solution():
    num_friends = 4
    num_donuts_per_friend = 3
    extra_donuts_per_friend = 1

    # Calculate the total number of donuts Andrew's mother needs to buy
    total_donuts = (num_friends * num_donuts_per_friend) + (num_friends * extra_donuts_per_friend)

    result = total_donuts
    return result

print(solution())