def solution():
    
    boxes = 10
    packs_per_box = 20
    tissues_per_pack = 100
    price_per_tissue = 0.05
    total_tissues = boxes * packs_per_box * tissues_per_pack
    total_cost = total_tissues * price_per_tissue
    result = total_cost
    return result

print(solution())