def solution():
    
    grown_pumpkins = 83
    carving_pumpkins_revenue = 96
    carving_pumpkins_sold = carving_pumpkins_revenue // 3
    total_pumpkins_sold = carving_pumpkins_sold + grown_pumpkins
    pie_filling_cans = (grown_pumpkins - carving_pumpkins_sold) // 3
    result = pie_filling_cans
    return result

print(solution())