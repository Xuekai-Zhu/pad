def solution():
    # Calculate the total number of donuts Andrew's mother needs to buy
    num_friends = 4  # Andrew invited 2 more friends, in addition to Brian and Samuel
    donuts_per_person = 4  # Andrew asked for 3 donuts for each friend, and his mother wants to buy one more for each friend
    total_donuts = num_friends * donuts_per_person  # total number of donuts needed for all friends
    result = total_donuts
    return result

print(solution())