def solution():
    # Calculate the amount of milk turned into sour cream and butter
    milk_sour_cream = 1/4 * 16  # 1/4 of the milk turned into sour cream
    milk_butter = 1/4 * 16  # 1/4 of the milk turned into butter
    milk_whole = 16 - milk_sour_cream - milk_butter  # rest of the milk kept as whole

    # Calculate the amount of sour cream and butter produced
    sour_cream = milk_sour_cream / 2  # 2 gallons of milk make 1 gallon of sour cream
    butter = milk_butter / 4  # 4 gallons of milk make 1 gallon of butter

    # Calculate total earnings from selling sour cream, butter, and whole milk
    earnings = (sour_cream * 6) + (butter * 5) + (milk_whole * 3)
    result = earnings
    return result

print(solution())