def solution():
    
    temp_50_yards = 20
    temp_80_yards = 2 * temp_50_yards
    saturday_throws = 20
    sunday_throws = 30
    saturday_yards = saturday_throws * temp_50_yards
    sunday_yards = sunday_throws * temp_80_yards
    total_yards = saturday_yards + sunday_yards
    result = total_yards
    return result

print(solution())