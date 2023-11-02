def solution():
    """Milly is making croissants. She needs to fold the dough 4 times, which takes 5 minutes each time, then let it rest for 75 minutes each time. If mixing the ingredients takes 10 minutes and baking the croissants takes 30 minutes, how many hours does the whole process take?"""
    folds = 4
    fold_time = 5
    rest_time = 75
    mixing_time = 10
    baking_time = 30
    total_time = (folds * fold_time * 2) + (rest_time * folds) + mixing_time + baking_time
    hours = total_time / 60
    result = hours
    return result

print(solution())