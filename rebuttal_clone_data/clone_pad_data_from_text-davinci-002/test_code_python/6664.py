def solution():
     toilet_paper_cost = 10 * 1.50
     paper_towel_cost = 7 * 2
     total_cost = 35
     tissue_cost = total_cost - (toilet_paper_cost + paper_towel_cost)
     result = tissue_cost
     return result

print(solution())