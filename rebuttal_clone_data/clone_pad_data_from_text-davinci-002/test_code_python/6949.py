def solution():
    chips_eaten = 10
    calories_per_chip = 60
    cheezits_eaten = 6
    calories_per_cheezit = (calories_per_chip * 4) / 3
    total_calories = (chips_eaten * calories_per_chip) + (cheezits_eaten * calories_per_cheezit)
    result = total_calories
    
    return result

print(solution())