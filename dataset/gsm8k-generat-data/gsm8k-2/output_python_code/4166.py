def solution():
    """Andrew is having two of his friends over for a sleepover. For one friend, Brian, he asks his mother to buy 3 donuts. He asks for his other friend, Samuel, to get the same. A day before the sleepover Andrew ends up inviting two more friends and asks his mother to buy them the same amount of donuts. Just in case, Andrew’s mother wants to buy one more donut for each of Andrew’s friends. Andrew’s mother is going to buy the same amount of donuts for Andrew as everybody else. How many donuts will Andrew’s mother need to buy?"""
    original_friends = 2
    original_donuts_per_friend = 3
    extra_friends = 2
    extra_donuts_per_friend = original_donuts_per_friend + 1
    total_friends = original_friends + extra_friends
    total_donuts = (original_donuts_per_friend + extra_donuts_per_friend) * total_friends
    result = total_donuts
    return result

print(solution())