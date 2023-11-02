def solution():
    """Jackson's oldest son gets 4 cookies after school and his youngest son gets 2 cookies after school. If there are 54 cookies in a box, how many days will the box last?"""
    # Define the number of cookies each day
    cookies_per_day = 4 + 2

    # Calculate the number of days the box will last
    days = 54 // cookies_per_day

    # Return the result
    result = days
    return result

print(solution())