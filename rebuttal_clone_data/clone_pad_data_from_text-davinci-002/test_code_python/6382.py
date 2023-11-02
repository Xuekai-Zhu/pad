def solution():
     camp_groups = 4
     group1_children = 14
     group2_children = 16
     group3_children = 12
     group4_children = (group1_children + group2_children + group3_children) / 2
     group1_water = group1_children * 3
     group2_water = group2_children * 3
     group3_water = group3_children * 3
     group4_water = group4_children * 3
     total_water = group1_water + group2_water + group3_water + group4_water
     bottles_per_case = 24
     cases_purchased = 13
     bottles_purchased = cases_purchased * bottles_per_case
     remaining_bottles = total_water - bottles_purchased
     result = remaining_bottles
     return result

print(solution())