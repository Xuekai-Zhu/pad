def solution():
    # Define the number of each item and its respective cost
    toilet_paper = 10
    toilet_paper_cost = 1.5
    paper_towels = 7
    paper_towels_cost = 2
    tissues = 3

    # Calculate the total cost of the items
    total_cost = (toilet_paper * toilet_paper_cost) + (paper_towels * paper_towels_cost)

    # Calculate the cost of one box of tissues
    tissue_cost = (35 - total_cost) / tissues
    result = tissue_cost
    return result

print(solution())