def solution():
    """Jules is walking dogs to help pay for his family's vacation. The vacation costs $1,000. There are five members in his family and each one must contribute the same amount towards the vacation cost. He charges $2 to start a walk and $1.25 per block. If he walks 20 dogs, how many blocks in total does he have to walk them?"""
    # Define the vacation cost and the number of family members
    VACATION_COST = 1000
    FAMILY_MEMBERS = 5

    # Calculate the amount each family member must contribute
    contribution_per_member = VACATION_COST / FAMILY_MEMBERS

    # Calculate the total revenue from dog walking
    total_revenue = 20 * (2 + 1.25 * 30)

    # Calculate the number of blocks Jules needs to walk the dogs
    blocks_to_walk = (total_revenue - contribution_per_member) / 1.25

    # Display the total number of blocks Jules needs to walk
    result = blocks_to_walk
    return result

print(solution())