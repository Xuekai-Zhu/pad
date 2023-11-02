def solution():
     difference = 400
     boys = 600
     girls = boys + difference
     percent_of_total = 60
     total = boys + girls
     sixty_percent_of_total = total * (percent_of_total / 100)
     result = sixty_percent_of_total
     return result

print(solution())