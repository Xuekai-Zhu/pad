def solution():
    """Bryan starts exercising at home during quarantine. To start, he decides to do 3 sets of 15 push-ups each. Near the end of the third set, he gets tired and does 5 fewer push-ups. How many push-ups did he do in total?"""
    sets = 3
    pushups_per_set = 15
    last_set_pushups = pushups_per_set - 5
    total_pushups = (pushups_per_set * (sets - 1)) + last_set_pushups
    result = total_pushups
    return result

print(solution())