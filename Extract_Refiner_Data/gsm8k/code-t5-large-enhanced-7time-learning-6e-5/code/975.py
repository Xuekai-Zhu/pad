def solution():
    
    emil_age = 19
    emil_turns_24 = 24
    dad_age_after_turn = emil_turns_24 / 2
    brother_age_after_turn = dad_age_after_turn / 2
    brother_age_now = brother_age_after_turn / 2
    total_dad_and_brother_age = dad_age_after_turn + brother_age_after_turn
    result = total_dad_and_brother_age
    return result

print(solution())