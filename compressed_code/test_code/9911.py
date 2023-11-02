def solution():
    
    total_cranes = 1000
    cranes_folded_by_alice = total_cranes / 2
    cranes_folded_by_friend = (total_cranes - cranes_folded_by_alice) / 5
    cranes_left_to_fold = total_cranes - cranes_folded_by_alice - cranes_folded_by_friend
    result = cranes_left_to_fold
    return result

print(solution())