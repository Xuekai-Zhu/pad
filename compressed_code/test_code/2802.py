def solution():
    
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