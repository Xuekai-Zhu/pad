def solution():
    """Camille goes to the Ice Cream Palace with her husband and two children. Each one orders a different ice cream. Camille orders a banana split, her husband orders a waffle bowl, her daughter orders a single cone, and her son orders a double cone. The cone has 1 scoop of ice cream, the banana split has 3 times as many scoops of ice cream as the cone and the waffle bowl has 1 more scoop than the banana split. How many scoops of ice cream did the ice cream man serve?"""
    cone_scoops = 1
    banana_split_scoops = 3 * cone_scoops
    waffle_bowl_scoops = banana_split_scoops + 1
    
    total_scoops = cone_scoops + banana_split_scoops + waffle_bowl_scoops + 2 # Add 2 for daughter and son
    
    result = total_scoops
    
    return result

print(solution())