def solution():
    vacation_cost = 1000
    family_members = 5
    amount_per_member = vacation_cost / family_members
    start_of_walk_fee = 2
    per_block_fee = 1.25
    blocks_ walked = (vacation_cost - start_of_walk_fee) / per_block_fee
    result = blocks_walked
    return result

print(solution())