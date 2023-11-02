def solution():
    
    total_cost = 100
    boss_contribution = 15
    todd_contribution = 2 * boss_contribution
    remaining_cost = total_cost - boss_contribution - todd_contribution
    num_remaining_workers = 5
    each_remaining_contribution = remaining_cost / num_remaining_workers
    result = each_remaining_contribution
    return result

print(solution())