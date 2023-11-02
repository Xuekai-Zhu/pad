def solution():
     cherry_sours = 32
     lemon_sours = cherry_sours * 5/4
     orange_sours = cherry_sours + lemon_sours * 1/4
     total_sours = cherry_sours + lemon_sours + orange_sours
     result = total_sours
     return result

print(solution())