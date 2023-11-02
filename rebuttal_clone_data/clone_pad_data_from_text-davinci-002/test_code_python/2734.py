def solution():
     basil_plants = 3
     rosemary_plants = 9
     thyme_plants = 6
     basil_leaves = 4
     rosemary_leaves = 18
     thyme_leaves = 30
     total_leaves = (basil_plants * basil_leaves) + (rosemary_plants * rosemary_leaves) + (thyme_plants * thyme_leaves)
     result = total_leaves
     return result

print(solution())