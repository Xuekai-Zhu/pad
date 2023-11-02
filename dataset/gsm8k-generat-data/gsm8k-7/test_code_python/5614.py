def solution():
    vacation_cost = 1000
    num_family_members = 5
    contribution_per_member = vacation_cost / num_family_members

    start_rate = 2
    rate_per_block = 1.25

    num_dogs = 20

    # Calculate the total earned from walking all the dogs
    total_earned = start_rate * num_dogs
    total_blocks = 0
    for dog in range(num_dogs):
        # Calculate the distance walked for each dog
        distance = (dog + 1) * 2

        # Add the distance walked to the total number of blocks
        total_blocks += distance

        # Add the amount earned from walking this dog to the total earned
        total_earned += distance * rate_per_block
    
    # Calculate the number of blocks Jules needs to walk in total
    result = total_blocks
    return result

print(solution())