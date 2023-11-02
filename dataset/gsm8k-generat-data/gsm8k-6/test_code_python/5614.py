def solution():
    # Calculate the total amount needed for the vacation
    vacation_cost = 1000
    num_family_members = 5
    amount_per_family_member = vacation_cost / num_family_members

    # Calculate the total revenue from walking 20 dogs
    num_dogs = 20
    start_walk_fee = 2
    per_block_fee = 1.25
    revenue = start_walk_fee * num_dogs + per_block_fee * num_dogs * 30  # assume each walk is 30 blocks

    # Calculate the total number of blocks needed to walk
    total_blocks = (revenue - amount_per_family_member * num_family_members) / (per_block_fee * num_dogs)
    result = total_blocks
    return result

print(solution())