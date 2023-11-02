def solution():
    
    chickens_foster = 45
    water_american = chickens_foster * 2
    chickens_hormel = chickens_foster * 3
    chickens_boudin = chickens_hormel / 3
    water_delmonte = water_american - 30
    total_items = chickens_foster + water_american + chickens_hormel + chickens_boudin + water_delmonte
    result = total_items
    return result

print(solution())