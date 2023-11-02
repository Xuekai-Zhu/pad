def solution():
     height = 65
     growth = 3
     percent = 10
     chance = percent + (percent * (growth / height))
     result = chance
     return result

print(solution())