def solution():
    
    toilet_paper_cost = 1.5
    paper_towel_cost = 2
    num_toilet_paper = 10
    num_paper_towels = 7
    num_tissues = 3
    total_cost = 35
    tissues_cost = (total_cost - (toilet_paper_cost*num_toilet_paper) - (paper_towel_cost*num_paper_towels)) / num_tissues
    result = tissues_cost
    return result

print(solution())