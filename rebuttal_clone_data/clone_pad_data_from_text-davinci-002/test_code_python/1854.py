def solution():
     bushel_weight = 56
     ear_of_corn_weight = .5
     cobs_per_bushel = bushel_weight / ear_of_corn_weight
     bushels_picked = 2
     total_cobs = cobs_per_bushel * bushels_picked
     result = total_cobs
     return result

print(solution())