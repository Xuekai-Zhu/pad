def solution():
     boxes_ordered = 10
     apples_per_box = 300
     boxes_sold = (boxes_ordered * 3) / 4
     apples_sold = boxes_sold * apples_per_box
     apples_leftover = (boxes_ordered * apples_per_box) - apples_sold
     result = apples_leftover
     return result

print(solution())