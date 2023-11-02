def solution():
    """The Tampa Bay Bucs have 13 football players and 16 cheerleaders. 
    If 10 football players and 4 cheerleaders quit, how many football players and cheerleaders are left?"""
    initial_fp = 13
    initial_cl = 16
    quit_fp = 10
    quit_cl = 4
    remaining_fp = initial_fp - quit_fp
    remaining_cl = initial_cl - quit_cl
    result = (remaining_fp, remaining_cl)
    return result

print(solution())