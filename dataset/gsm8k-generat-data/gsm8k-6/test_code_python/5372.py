def solution():
    # Calculate the total amount of money Annalise spent
    packs_per_box = 20
    tissues_per_pack = 100
    cost_per_tissue = 0.05
    boxes = 10
    total_packs = packs_per_box * boxes
    total_tissues = total_packs * tissues_per_pack
    total_cost = total_tissues * cost_per_tissue
    result = total_cost
    return result

print(solution())