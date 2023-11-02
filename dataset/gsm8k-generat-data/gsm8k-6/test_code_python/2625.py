def solution():
    # Calculate the total number of Toby's friends
    total_friends = 33 / (55/100)  # calculate the percentage of boys and use it to find the total number of friends
    girls_friends = total_friends - 33  # the remaining friends are girls
    result = girls_friends
    return result

print(solution())