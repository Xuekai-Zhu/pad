def solution():
    total_pencils = 30  # Charley bought 30 pencils
    lost_during_move = 6  # Charley lost 6 pencils during her move
    remaining_pencils = total_pencils - lost_during_move  # Charley has this many pencils left after her move
    lost_1_3 = remaining_pencils / 3  # Charley lost 1/3 of the remaining pencils
    current_pencils = remaining_pencils - lost_1_3  # Charley currently has this many pencils left

    result = current_pencils
    return result

print(solution())