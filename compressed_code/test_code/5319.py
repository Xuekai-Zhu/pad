def solution():
    
    herring_fat = 40
    eel_fat = 20
    pike_fat = eel_fat + 10
    total_herring_fat = herring_fat * 40
    total_eel_fat = eel_fat * 40
    total_pike_fat = pike_fat * 40
    total_fat = total_herring_fat + total_eel_fat + total_pike_fat
    result = total_fat
    return result

print(solution())