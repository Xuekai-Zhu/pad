def solution():
    
    cone_scoops = 1
    banana_split_scoops = 3 * cone_scoops
    waffle_bowl_scoops = banana_split_scoops + 1
    
    total_scoops = cone_scoops + banana_split_scoops + waffle_bowl_scoops + 2 
    
    result = total_scoops
    
    return result

print(solution())