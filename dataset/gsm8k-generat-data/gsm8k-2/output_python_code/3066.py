def solution():
    """Stefan, Vail, and Aiguo collected seashells. Stefan had 16 more seashells than Vail. Vail had 5 less than Aiguo. Aiguo had 20 seashells. How many seashells did the 3 children have in total?"""
    aiguo_seashells = 20
    vail_seashells = aiguo_seashells - 5
    stefan_seashells = vail_seashells + 16
    total_seashells = aiguo_seashells + vail_seashells + stefan_seashells
    result = total_seashells
    return result

print(solution())