def solution():
    
    flour_per_pound = 2
    pasta_per_rack = 3
    racks_owned = 3
    flour_used = 3 * 8
    pasta_made = flour_used / flour_per_pound
    racks_needed = pasta_made / pasta_per_rack
    additional_racks_needed = racks_needed - racks_owned
    result = additional_racks_needed
    return result

print(solution())