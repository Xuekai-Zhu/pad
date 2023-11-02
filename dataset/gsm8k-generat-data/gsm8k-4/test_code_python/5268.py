def solution():
    """Pat's Pool Supply has three times as many swimming pools as Pat's Ark & Athletic Wear store. If Pat's Ark & Athletic Wear store has 200 pools, how many pools do they have in total?"""
    # Define the number of pools at Pat's Ark & Athletic Wear store
    ark_pools = 200

    # Calculate the number of pools at Pat's Pool Supply
    pool_supply_pools = 3 * ark_pools

    # Calculate the total number of pools
    total_pools = ark_pools + pool_supply_pools

    result = total_pools
    return result

print(solution())