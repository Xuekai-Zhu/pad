def solution():
    """It takes 50 minutes to cut a woman's hair, 15 minutes to cut a man's hair, and 25 minutes to cut a kid's hair. If Joe cut 3 women's, 2 men's, and 3 children's hair, how much time did he spend cutting hair?"""
    women_time = 50 * 3
    men_time = 15 * 2
    children_time = 25 * 3
    total_time = women_time + men_time + children_time
    result = total_time
    return result

print(solution())