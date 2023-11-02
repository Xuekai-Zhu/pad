def solution():
    # Calculate the total number of toys Joel collected from his friends
    friends_toys = 18 + 42 + 2 + 13

    # Calculate the number of toys Joel's sister donated
    sister_toys = 108 - friends_toys
    sister_toys_from_closet = sister_toys / 3

    # Calculate the number of toys Joel donated
    joel_toys = (sister_toys_from_closet * 2) + sister_toys_from_closet

    result = joel_toys
    return result

print(solution())