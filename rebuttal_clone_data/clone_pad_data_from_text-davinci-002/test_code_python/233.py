def solution():
    """Bryan starts exercising at home during quarantine. To start, he decides to do 3 sets of 15 push-ups each. Near the end of the third set, he gets tired and does 5 fewer push-ups. How many push-ups did he do in total?"""
    sets_of_pushups = 3
    pushups_per_set = 15
    pushups_in_third_set = pushups_per_set - 5
    total_pushups = sets_of_pushups * pushups_per_set + pushups_in_third_set
    result = total_pushups
    return result

print(solution())