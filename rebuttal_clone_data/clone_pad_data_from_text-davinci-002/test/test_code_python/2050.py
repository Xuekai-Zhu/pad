def solution():
     total_chickens = 440
     roosters = 39
     hens = total_chickens - roosters
     non_laying_hens = 15
     laying_hens = hens - non_laying_hens
     eggs_per_hen = 3
     total_eggs = laying_hens * eggs_per_hen
     result = total_eggs
     return result

print(solution())