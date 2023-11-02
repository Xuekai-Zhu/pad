def solution():
    # Define the amount of fat in each type of fish
    herring_fat = 40
    eel_fat = 20
    pike_fat = eel_fat + 10

    # Calculate the total amount of fat served
    total_fat = (herring_fat + eel_fat + pike_fat) * 40

    result = total_fat
    return result

print(solution())