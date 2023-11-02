def solution():
    cost_per_pack = 3
    cards_per_pack = 50
    cards_given_out = 10
    classes_per_day = 6
    students_per_class = 30
    total_students = classes_per_day * students_per_class
    total_cards = total_students * cards_given_out
    total_packs = total_cards / cards_per_pack
    total_cost = total_packs * cost_per_pack
    result = total_cost
    return result

print(solution())