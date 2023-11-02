def solution():
     backpack = 15
     pens = 1
     pencils = 1
     notebooks = (32 - (backpack + pens + pencils)) / 5
     result = notebooks
     return result

print(solution())