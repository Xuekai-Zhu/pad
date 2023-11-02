def solution():
    herring_fat = 40
    eel_fat = 20
    pike_fat = eel_fat + 10
    num_fish = 40

    # Calculate the total ounces of fat from the herrings
    total_herring_fat = herring_fat * num_fish

    # Calculate the total ounces of fat from the eels
    total_eel_fat = eel_fat * num_fish

    # Calculate the total ounces of fat from the pikes
    total_pike_fat = pike_fat * num_fish

    # Calculate the total ounces of fat served
    total_fat = total_herring_fat + total_eel_fat + total_pike_fat
    result = total_fat
    return result

print(solution())