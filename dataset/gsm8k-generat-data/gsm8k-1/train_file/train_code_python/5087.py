def solution():
    """Barbara went shopping in a supermarket. She bought 5 packs of tuna for $2 each and 4 bottles of water for $1.5 each. In total, she paid $56 for her shopping. How much did Barbara spend on different than the mentioned goods?"""
    packs_of_tuna = 5
    cost_per_pack_of_tuna = 2
    bottles_of_water = 4
    cost_per_bottle_of_water = 1.5
    total_cost = 56
    
    cost_of_tuna = packs_of_tuna * cost_per_pack_of_tuna
    cost_of_water = bottles_of_water * cost_per_bottle_of_water
    cost_of_others = total_cost - cost_of_tuna - cost_of_water
    
    result = cost_of_others
    return result

print(solution())