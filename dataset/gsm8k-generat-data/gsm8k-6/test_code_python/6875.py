def solution():
    herring_fat = 40 #oz of fat in herring
    eel_fat = 20 #oz of fat in eel
    pike_fat = eel_fat + 10 #oz of fat in pike
    
    num_of_fish = 40 #number of fish of each type
    
    total_herring_fat = herring_fat * num_of_fish #total oz of fat in herring
    total_eel_fat = eel_fat * num_of_fish #total oz of fat in eel
    total_pike_fat = pike_fat * num_of_fish #total oz of fat in pike
    
    total_fat = total_herring_fat + total_eel_fat + total_pike_fat #total oz of fat in all fish
    
    result = total_fat
    return result

print(solution())