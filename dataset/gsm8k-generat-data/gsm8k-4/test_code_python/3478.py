def solution():
    """Pat is buying supplies for S'mores. He and his friends will each eat 3 S'mores. There are 8 of them in total. It costs $3 in supplies to make 4 S'mores. How much will it cost to buy all the supplies?"""
    # Define the number of people and S'mores needed
    num_people = 8
    smores_per_person = 3
    total_smores = num_people * smores_per_person

    # Define the cost per batch of 4 S'mores and calculate the total cost
    cost_per_batch = 3
    batches_needed = total_smores // 4 + (1 if total_smores % 4 > 0 else 0)
    total_cost = batches_needed * cost_per_batch

    # Return the total cost
    return total_cost

print(solution())