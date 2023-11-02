def solution():
    """Milly is making croissants. She needs to fold the dough 4 times, which takes 5 minutes each time, then let it rest for 75 minutes each time. If mixing the ingredients takes 10 minutes and baking the croissants takes 30 minutes, how many hours does the whole process take?"""
    fold_time = 4 * 5
    rest_time = 4 * 75
    mix_time = 10
    bake_time = 30
    total_time = fold_time + rest_time + mix_time + bake_time
    result = total_time / 60
    return result

print(solution())