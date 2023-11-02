def solution():
     cost = 300
     sale = 255
     percent_lost = ((cost - sale) / cost) * 100
     result = percent_lost
     return result

print(solution())