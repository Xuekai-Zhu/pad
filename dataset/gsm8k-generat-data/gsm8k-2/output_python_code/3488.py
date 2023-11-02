def solution():
    """Enrique has 2 132 contracts that he needs to shred. His paper shredder will only allow him to shred 6 pages at a time. How many times will he shred 6 units of paper until all of the contracts are shredded?"""
    contract_size = 2132
    shredder_capacity = 6
    total_shreds = contract_size // shredder_capacity
    if contract_size % shredder_capacity != 0:
        total_shreds += 1
    result = total_shreds
    return result

print(solution())