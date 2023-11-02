def solution():
    # Total fat for each type of fish
    herring_fat = 40
    eel_fat = 20
    pike_fat = eel_fat + 10

    # Calculate the total fat for each type of fish served
    total_herring_fat = herring_fat * 40  # 40 herring served
    total_eel_fat = eel_fat * 40  # 40 eel served
    total_pike_fat = pike_fat * 40  # 40 pike served

    # Calculate the total fat served
    total_fat = total_herring_fat + total_eel_fat + total_pike_fat
    result = total_fat
    return result

print(solution())