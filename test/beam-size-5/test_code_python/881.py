def solution():
    
    tuesdays_chimichangas = 125
    wednesdays_chimichangas = 125
    friday_chimichangas = 2 * tuesdays_chimichangas
    total_chimichangas = tuesdays_chimichangas + wednesdays_chimichangas + friday_chimichangas
    result = total_chimichangas
    return result

print(solution())