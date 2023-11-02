def solution():
    """Jules is walking dogs to help pay for his family's vacation. The vacation costs $1,000. There are five members in his family and each one must contribute the same amount towards the vacation cost. He charges $2 to start a walk and $1.25 per block. If he walks 20 dogs, how many blocks in total does he have to walk them?"""
    vacation_cost = 1000
    num_family_members = 5
    contribution_per_person = vacation_cost / num_family_members
    start_cost = 2
    cost_per_block = 1.25
    total_blocks_to_walk = (contribution_per_person - start_cost) / cost_per_block / 20
    result = total_blocks_to_walk
    return result

print(solution())