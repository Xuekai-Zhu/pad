def solution():
    """Natalie's sister had 8 small diaries in her locker. Last summer she bought double the number of diaries she had and then lost 1/4 of what she had. How many diaries does Natalie's sister have now?"""
    # Define the initial number of diaries
    initial_diaries = 8

    # Calculate the number of diaries Natalie's sister bought
    bought_diaries = 2 * initial_diaries

    # Calculate the number of diaries Natalie's sister lost
    lost_diaries = bought_diaries * 0.25

    # Calculate the current number of diaries Natalie's sister has
    current_diaries = bought_diaries - lost_diaries

    # Display the current number of diaries
    result = current_diaries
    return result

print(solution())