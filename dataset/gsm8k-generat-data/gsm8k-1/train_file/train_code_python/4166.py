def solution():
    """Andrew is having two of his friends over for a sleepover. For one friend, Brian, he asks his mother to buy 3 donuts. He asks for his other friend, Samuel, to get the same. A day before the sleepover Andrew ends up inviting two more friends and asks his mother to buy them the same amount of donuts. Just in case, Andrew’s mother wants to buy one more donut for each of Andrew’s friends. Andrew’s mother is going to buy the same amount of donuts for Andrew as everybody else. How many donuts will Andrew’s mother need to buy?"""
    donuts_per_friend = 3
    friends_invited = 4
    total_friends = friends_invited + 2  # Andrew's two friends
    total_donuts = (donuts_per_friend * total_friends) + total_friends  # adding one extra donut for each friend
    result = total_donuts
    return result

print(solution())