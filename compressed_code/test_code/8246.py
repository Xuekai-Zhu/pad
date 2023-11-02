def solution():
    
    num_students = 20
    num_packs = num_students
    crackers_per_pack = 10
    num_unopened_packs = 2
    num_opened_packs = num_packs - num_unopened_packs
    total_crackers = num_opened_packs * crackers_per_pack
    result = total_crackers
    return result

print(solution())