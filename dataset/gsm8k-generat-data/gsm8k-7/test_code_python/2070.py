def solution():
    num_packs = 80
    expired_percentage = 0.4
    pack_cost = 12.0

    # Calculate the number of packs that are expired
    num_expired_packs = num_packs * expired_percentage

    # Calculate the cost of the expired packs
    expired_packs_cost = num_expired_packs * pack_cost

    result = expired_packs_cost
    return result

print(solution())