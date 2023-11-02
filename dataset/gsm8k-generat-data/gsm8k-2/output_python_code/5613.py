def solution():
    """Jules is walking dogs to help pay for his family's vacation. The vacation costs $1,000. There are five members in his family and each one must contribute the same amount towards the vacation cost. He charges $2 to start a walk and $1.25 per block. If he walks 20 dogs, how many blocks in total does he have to walk them?"""
    vacation_cost = 1000
    family_members = 5
    per_person_cost = vacation_cost / family_members
    dog_walk_cost = 2 + (1.25 * 20)
    blocks_to_walk = per_person_cost / dog_walk_cost
    result = blocks_to_walk
    return result

print(solution())