def solution():
    # Calculate the total number of toys Joel collected from his friends
    total_friends_toys = 18 + 42 + 2 + 13

    # Calculate the number of toys Joel's sister donated
    sister_toys = (108 - total_friends_toys) / 3

    # Calculate the number of toys Joel donated, including his own
    joel_toys = sister_toys * 3

    result = joel_toys
    return result

print(solution())