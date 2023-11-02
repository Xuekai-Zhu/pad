def solution():
    """Natalie's sister had 8 small diaries in her locker. Last summer she bought double the number of diaries she had and then lost 1/4 of what she had. How many diaries does Natalie's sister have now?"""
    # Initialize the starting number of diaries
    num_diaries = 8

    # Calculate the number of diaries bought last summer
    num_bought = num_diaries * 2

    # Calculate the number of diaries lost
    num_lost = num_bought * 0.25

    # Calculate the number of diaries left
    num_left = num_bought - num_lost

    # Add the starting number of diaries to get the total number of diaries
    total_diaries = num_left + num_diaries

    result = total_diaries
    return result

print(solution())