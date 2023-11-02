def solution():
    num_boxes = 10
    num_packs_per_box = 20
    num_tissues_per_pack = 100
    cost_per_tissue = 0.05

    # Calculate the total number of tissues Annalise purchased
    total_tissues = num_boxes * num_packs_per_box * num_tissues_per_pack

    # Calculate the total cost of the tissues
    total_cost = total_tissues * cost_per_tissue

    result = total_cost
    return result

print(solution())