def solution():
    """Bryan starts exercising at home during quarantine. To start, he decides to do 3 sets of 15 push-ups each. Near the end of the third set, he gets tired and does 5 fewer push-ups. How many push-ups did he do in total?"""
    set1 = 15
    set2 = 15
    set3 = 15 - 5 # tired near the end
    total_pushups = set1 + set2 + set3
    result = total_pushups
    return result

print(solution())