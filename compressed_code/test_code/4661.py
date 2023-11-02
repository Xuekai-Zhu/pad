def solution():
    
    total_burritos = 3 * 20
    given_away = total_burritos / 3
    remaining_burritos = total_burritos - given_away
    eaten_burritos = 3 * 10
    final_burritos = remaining_burritos - eaten_burritos
    result = final_burritos
    return result

print(solution())