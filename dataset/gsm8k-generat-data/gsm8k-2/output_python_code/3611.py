def solution():
    """Carl buys index cards for his class. He gives each student 10 index cards. He teaches 6 periods a day and each class has 30 students. If a 50 pack of index cards cost $3 how much did he spend on them all?"""
    num_students = 30
    num_periods = 6
    cards_per_student = 10
    cards_per_pack = 50
    cost_per_pack = 3
    total_cards = num_students * num_periods * cards_per_student
    total_packs = total_cards // cards_per_pack + (1 if total_cards % cards_per_pack != 0 else 0)
    total_cost = total_packs * cost_per_pack
    result = total_cost
    return result

print(solution())