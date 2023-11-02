def solution():
    num_contracts = 2
    num_units_per_contract = 132
    units_per_shred = 6

    # Calculate the total number of units of paper that need to be shredded
    total_units = num_contracts * num_units_per_contract

    # Calculate the number of times he needs to shred 6 units of paper to shred all the contracts
    num_shreds = total_units // units_per_shred
    if total_units % units_per_shred != 0:
        num_shreds += 1

    result = num_shreds
    return result

print(solution())