def solution():
    korean_ships = 150
    korean_aircraft = 70
    korean_personnel = 70000
    korean_marines = 29000
    
    eritrean_ships = 4
    eritrean_army = 45000
    
    # Check if the Korean Navy has more ships, aircraft, and personnel than the Eritrean Navy and army combined
    if korean_ships + korean_aircraft + korean_personnel + korean_marines > eritrean_ships + eritrean_army:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())