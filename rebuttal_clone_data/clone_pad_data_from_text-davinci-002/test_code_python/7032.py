def solution():
     donuts_bought = 2.5 * 12
     donuts_eaten = 0.1 * donuts_bought
     donuts_snacked = 4
     donuts_left = donuts_bought - donuts_eaten - donuts_snacked
     result = donuts_left
     return result

print(solution())