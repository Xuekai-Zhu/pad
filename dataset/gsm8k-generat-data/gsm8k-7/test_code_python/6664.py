def solution():
    num_toilet_paper = 10
    toilet_paper_price = 1.5

    num_paper_towels = 7
    paper_towels_price = 2

    num_tissue_boxes = 3

    total_cost = 35

    # Calculate the total cost of all toilet paper
    total_toilet_paper_cost = num_toilet_paper * toilet_paper_price

    # Calculate the total cost of all paper towels
    total_paper_towels_cost = num_paper_towels * paper_towels_price

    # Calculate the total cost of all tissue boxes
    total_tissue_boxes_cost = total_cost - total_toilet_paper_cost - total_paper_towels_cost

    # Calculate the cost of one box of tissues
    tissue_box_cost = total_tissue_boxes_cost / num_tissue_boxes
    result = tissue_box_cost
    return result

print(solution())