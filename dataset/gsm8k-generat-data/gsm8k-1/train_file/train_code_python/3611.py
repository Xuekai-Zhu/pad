def solution():
    """Carl buys index cards for his class. He gives each student 10 index cards. He teaches 6 periods a day and each class has 30 students. If a 50 pack of index cards cost $3 how much did he spend on them all?"""
    cards_per_student = 10
    periods_per_day = 6
    students_per_period = 30
    packs_per_period = (cards_per_student * students_per_period) // 50 + 1
    total_packs = packs_per_period * periods_per_day
    cost_per_pack = 3
    total_cost = total_packs * cost_per_pack
    result = total_cost
    return result

print(solution())