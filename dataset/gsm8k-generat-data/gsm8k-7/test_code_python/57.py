def solution():
    total_butter = 10
    used_for_choco = total_butter / 2
    used_for_peanut = total_butter / 5
    remaining_butter = total_butter - used_for_choco - used_for_peanut
    used_for_sugar = remaining_butter / 3
    butter_left = remaining_butter - used_for_sugar
    result = butter_left
    return result

print(solution())