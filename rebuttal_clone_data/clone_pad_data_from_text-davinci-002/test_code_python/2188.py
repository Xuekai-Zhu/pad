def solution():
     antacid1_weight = 2
     antacid2_weight = 2
     antacid3_weight = 1
     antacid4_weight = 1
     antacid5_weight = 1
     antacid1_zinc = antacid1_weight * 0.05
     antacid2_zinc = antacid2_weight * 0.05
     antacid3_zinc = antacid3_weight * 0.15
     antacid4_zinc = antacid4_weight * 0.15
     antacid5_zinc = antacid5_weight * 0.15
     total_zinc = antacid1_zinc + antacid2_zinc + antacid3_zinc + antacid4_zinc + antacid5_zinc
     result = total_zinc
     return result

print(solution())