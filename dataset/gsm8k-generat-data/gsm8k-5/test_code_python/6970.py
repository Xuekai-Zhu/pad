def solution():
    # Calculate the total number of toys Joel collected from his friends
    toys_from_friends = 18 + 42 + 2 + 13
    # Calculate the number of toys Joel received from his sister
    toys_from_sister = (108 - toys_from_friends) / 3
    # Calculate the number of toys Joel donated from his own collection
    toys_from_joel = 2 * toys_from_sister
    # Calculate the total number of donated toys that were Joel's
    total_from_joel = toys_from_joel + toys_from_sister
    result = total_from_joel
    return result

print(solution())