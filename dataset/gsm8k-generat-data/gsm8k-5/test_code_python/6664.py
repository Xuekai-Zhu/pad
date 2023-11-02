def solution():
    rolls_of_toilet_paper = 10
    rolls_of_paper_towels = 7
    boxes_of_tissues = 3
    cost_of_toilet_paper = 1.5
    cost_of_paper_towels = 2
    total_cost = 35

    # Calculate the total cost of toilet paper and paper towels
    cost_of_toilet_paper_total = rolls_of_toilet_paper * cost_of_toilet_paper
    cost_of_paper_towels_total = rolls_of_paper_towels * cost_of_paper_towels

    # Calculate the cost of the tissues
    cost_of_tissues_total = total_cost - cost_of_toilet_paper_total - cost_of_paper_towels_total
    cost_per_box_of_tissues = cost_of_tissues_total / boxes_of_tissues
    result = cost_per_box_of_tissues
    return result

print(solution())