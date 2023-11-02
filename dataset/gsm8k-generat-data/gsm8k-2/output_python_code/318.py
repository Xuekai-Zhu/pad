def solution():
    """Natalie's sister had 8 small diaries in her locker. Last summer she bought double the number of diaries she had and then lost 1/4 of what she had. How many diaries does Natalie's sister have now?"""
    starting_diaries = 8
    bought_diaries = starting_diaries * 2
    lost_diaries = bought_diaries * 0.25
    current_diaries = bought_diaries - lost_diaries
    result = current_diaries
    return result

print(solution())