def solution():
    num_boxes = 10
    packs_per_box = 20
    tissues_per_pack = 100
    cost_per_tissue = 0.05

    # Calculate the total number of tissues Annalise bought
    total_tissues = num_boxes * packs_per_box * tissues_per_pack

    # Calculate the total cost of all tissues Annalise bought
    total_cost = total_tissues * cost_per_tissue
    result = total_cost
    return result

print(solution())