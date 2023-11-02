def solution():
    
    total_ducks = 320
    fox_eaten = total_ducks // 4
    remaining_ducks = total_ducks - fox_eaten
    flying_away = remaining_ducks // 6
    remaining_ducks -= flying_away
    stolen = int(remaining_ducks * 0.3)
    remaining_ducks -= stolen
    result = remaining_ducks
    return result

print(solution())