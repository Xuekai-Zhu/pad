def solution():
     apples_per_crate = 180
     crates_delivered = 12
     apples_rotten = 160
     apples_good = apples_per_crate * crates_delivered - apples_rotten
     apples_per_box = 20
     boxes_of_apples = apples_good // apples_per_box
     result = boxes_of_apples
     return result

print(solution())