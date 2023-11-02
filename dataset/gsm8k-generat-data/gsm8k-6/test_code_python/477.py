def solution():
    # Calculate the number of guests invited by the bride and groom
    guests_invited = 20 * 2  # the bride and groom each invited 20 couples, which is 40 guests in total

    # Calculate the number of friends who attended the reception
    friends_attended = 180 - guests_invited  # all remaining guests are friends
    result = friends_attended
    return result

print(solution())