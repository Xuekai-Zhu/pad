def solution():
     initial_cabinets = 3
     cabinets_installed_1 = 2 * initial_cabinets
     cabinets_installed_2 = cabinets_installed_1 / 3
     total_cabinets = initial_cabinets + cabinets_installed_1 + cabinets_installed_2 + 5
     result = total_cabinets
     return result

print(solution())