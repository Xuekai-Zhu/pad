def solution():
    """There are 70 cookies in a jar. If there are only 28 cookies left after a week, and Paul took out the same amount each day, how many cookies did he take out in four days?"""
    # Calculate the number of cookies Paul took out in one day
    cookies_per_day = (70 - 28) / 7

    # Calculate the number of cookies Paul took out in four days
    cookies_in_four_days = cookies_per_day * 4

    # Return the result
    result = cookies_in_four_days
    return result

print(solution())