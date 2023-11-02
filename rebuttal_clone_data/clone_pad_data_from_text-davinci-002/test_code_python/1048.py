def solution():
     total_barrels = 1200
     barrels_used = 150 + (2 * 150) + (2 * 150) + 100
     barrels_left = total_barrels - barrels_used
     result = barrels_left
     return result

print(solution())