def solution():
    kelsey_tray = 2/5
    stephanie_tray = 1/2
    alayah_tray = (kelsey_tray + stephanie_tray + 40)/30 # assuming one tray has 30 eggs
    willa_trays = 2
    total_eggs = (kelsey_tray + stephanie_tray + alayah_tray + willa_trays) * 30 # converting to number of eggs
    result = total_eggs
    return result

print(solution())