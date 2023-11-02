def solution():
    """The number of Christmas presents David found was twice as many as the number of birthday presents. If David found a total of 60 Christmas presents, how many presents did he get all together?"""
    # Define the ratio of Christmas presents to birthday presents
    ratio = 2

    # Calculate the number of birthday presents
    birthday_presents = 60 / (ratio + 1)

    # Calculate the total number of presents
    total_presents = birthday_presents * (ratio + 1)

    result = total_presents
    return result

print(solution())