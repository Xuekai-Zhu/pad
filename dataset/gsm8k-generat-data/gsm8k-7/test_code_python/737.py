def solution():
    num_packs = 4
    price_per_pack = 2.5
    additional_packs = 2

    # Calculate the total number of packs of crayons Michael will have
    total_packs = num_packs + additional_packs

    # Calculate the total worth of all packs of crayons Michael will have
    total_worth = total_packs * price_per_pack
    result = total_worth
    return result

print(solution())