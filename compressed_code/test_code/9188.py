def solution():
    
    bedroom_bulbs = 2
    bathroom_bulbs = 1
    kitchen_bulbs = 1
    basement_bulbs = 4
    garage_bulbs = (bedroom_bulbs + bathroom_bulbs + kitchen_bulbs + basement_bulbs) / 2
    total_bulbs = bedroom_bulbs + bathroom_bulbs + kitchen_bulbs + basement_bulbs + garage_bulbs
    bulbs_per_pack = 2
    packs_needed = total_bulbs // bulbs_per_pack
    result = packs_needed
    return result

print(solution())