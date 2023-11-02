def solution():
    Jacob_start = 8
    Alex_start = Jacob_start * 7
    fish_lost_by_Alex = 23
    Alex_end = Alex_start - fish_lost_by_Alex
    Jacob_need = Alex_end + 1 - Jacob_start
    result = Jacob_need 
    return result

print(solution())