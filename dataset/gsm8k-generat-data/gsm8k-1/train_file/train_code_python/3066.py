def solution():
    """Stefan, Vail, and Aiguo collected seashells. Stefan had 16 more seashells than Vail. Vail had 5 less than Aiguo. Aiguo had 20 seashells. How many seashells did the 3 children have in total?"""
    aiguo = 20
    vail = aiguo - 5
    stefan = vail + 16
    total_seashells = aiguo + vail + stefan
    result = total_seashells
    return result

print(solution())