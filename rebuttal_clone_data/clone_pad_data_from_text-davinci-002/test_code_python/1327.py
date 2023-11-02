def solution():
    first_turn_yards = 180
    second_turn_yards = first_turn_yards / 2
    second_turn_yards = second_turn_yards + 20
    third_turn_yards = 0
    total_yards = first_turn_yards + second_turn_yards + third_turn_yards
    result = total_yards
    return result

print(solution())