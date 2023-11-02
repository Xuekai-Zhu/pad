def solution():
    # Define the current number of packs of crayons
    current_packs = 4

    # Define the cost of one pack of crayons
    pack_cost = 2.5

    # Define the number of additional packs to buy
    additional_packs = 2

    # Calculate the new total number of packs
    total_packs = current_packs + additional_packs

    # Calculate the total cost of all the packs
    total_cost = total_packs * pack_cost
    result = total_cost
    return result

print(solution())