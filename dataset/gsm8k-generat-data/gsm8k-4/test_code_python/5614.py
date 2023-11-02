def solution():
    """Jules is walking dogs to help pay for his family's vacation. The vacation costs $1,000. There are five members in his family and each one must contribute the same amount towards the vacation cost. He charges $2 to start a walk and $1.25 per block. If he walks 20 dogs, how many blocks in total does he have to walk them?"""
    # Define the vacation cost and the number of family members
    vacation_cost = 1000
    num_family_members = 5

    # Calculate the amount each family member needs to contribute
    contribution = vacation_cost / num_family_members

    # Define the cost per dog walk
    dog_walk_cost = 2 + 1.25 * 20

    # Calculate the total blocks Jules needs to walk the dogs
    total_blocks = dog_walk_cost / 1.25

    result = total_blocks
    return result

print(solution())