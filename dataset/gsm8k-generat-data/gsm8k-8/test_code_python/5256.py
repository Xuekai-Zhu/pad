def solution():
    total_cranes = 1000
    alice_cranes = total_cranes / 2
    remaining_cranes = total_cranes - alice_cranes
    friend_cranes = remaining_cranes / 5
    still_need_to_fold = remaining_cranes - friend_cranes
    result = still_need_to_fold
    return result

print(solution())