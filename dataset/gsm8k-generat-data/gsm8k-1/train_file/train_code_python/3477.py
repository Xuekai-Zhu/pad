def solution():
    """Pat is buying supplies for S'mores. He and his friends will each eat 3 S'mores. 
    There are 8 of them in total. It costs $3 in supplies to make 4 S'mores. 
    How much will it cost to buy all the supplies?"""
    s_mores_per_person = 3
    total_people = 8
    s_mores_total = s_mores_per_person * total_people
    s_mores_per_batch = 4
    batches_needed = s_mores_total / s_mores_per_batch
    cost_per_batch = 3
    total_cost = batches_needed * cost_per_batch
    result = total_cost
    return result

print(solution())