def solution():
    # Calculate the total number of pools between the two stores
    pools_Ark = 200  # Pat's Ark & Athletic Wear store has 200 pools
    pools_Supply = 3 * pools_Ark  # Pat's Pool Supply has three times as many pools as Pat's Ark & Athletic Wear store
    total_pools = pools_Ark + pools_Supply
    
    result = total_pools
    return result

print(solution())