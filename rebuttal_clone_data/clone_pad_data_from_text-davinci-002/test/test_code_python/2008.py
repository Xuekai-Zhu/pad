def solution():
     total_seedlings = 1200
     seedlings_planted_by_remi = 200 + (2 * 200)
     seedlings_planted_by_father = total_seedlings - seedlings_planted_by_remi
     result = seedlings_planted_by_father
     
     return result

print(solution())