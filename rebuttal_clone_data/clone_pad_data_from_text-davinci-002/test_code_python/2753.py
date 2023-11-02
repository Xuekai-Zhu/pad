def solution():
     spiders = 3
     ants = 50
     eyes_per_spider = 8
     eyes_per_ant = 2
     total_eyes = (spiders * eyes_per_spider) + (ants * eyes_per_ant)
     result = total_eyes
     return result

print(solution())