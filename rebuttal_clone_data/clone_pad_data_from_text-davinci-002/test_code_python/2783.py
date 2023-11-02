def solution():
     chairs = 3
     table = 50
     plates = 2
     cost_of_chairs = (130 - (table + (plates * 20))) / chairs
     result = cost_of_chairs
     return result

print(solution())