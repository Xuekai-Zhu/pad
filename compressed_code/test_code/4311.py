def solution():
    
    first_place_points = 12 * 2 + 4 * 1
    second_place_points = 13 * 2 + 1 * 1
    elsa_points = 8 * 2 + 10 * 1
    playoff_points = first_place_points + second_place_points + elsa_points
    avg_points = playoff_points / 3
    result = avg_points
    return result

print(solution())