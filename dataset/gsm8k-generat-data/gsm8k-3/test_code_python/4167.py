def solution():
    """Andrew is having two of his friends over for a sleepover. For one friend, Brian, he asks his mother to buy 3 donuts. He asks for his other friend, Samuel, to get the same. A day before the sleepover Andrew ends up inviting two more friends and asks his mother to buy them the same amount of donuts. Just in case, Andrew’s mother wants to buy one more donut for each of Andrew’s friends. Andrew’s mother is going to buy the same amount of donuts for Andrew as everybody else. How many donuts will Andrew’s mother need to buy?"""
    # Define the number of donuts for each friend
    donuts_per_friend = 3

    # Define the number of friends
    num_friends = 4

    # Calculate the total number of donuts needed
    total_donuts = (donuts_per_friend + 1) * num_friends

    # Display the total number of donuts
    result = total_donuts
    return result

print(solution())