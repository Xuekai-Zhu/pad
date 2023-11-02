def solution():
    """Two friends are playing pick-up sticks. While playing, they noticed that there are 9 red sticks, and 5 more blue sticks than red. Also, the number of yellow sticks is 3 less than the blue sticks. How many sticks do they have?"""
    red_sticks = 9
    blue_sticks = red_sticks + 5
    yellow_sticks = blue_sticks - 3
    total_sticks = red_sticks + blue_sticks + yellow_sticks
    result = total_sticks
    return result

print(solution())