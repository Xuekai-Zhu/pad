def solution():
     total_judges = 40
     judges_under_30 = total_judges * 0.1
     judges_30_50 = total_judges * 0.6
     judges_over_50 = total_judges - (judges_under_30 + judges_30_50)
     result = judges_over_50
     return result

print(solution())