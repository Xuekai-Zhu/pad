def solution():
    num_christmas_presents = 60
    ratio_birthday_to_christmas = 1 / 2

    # Calculate the number of birthday presents
    num_birthday_presents = num_christmas_presents * ratio_birthday_to_christmas

    # Calculate the total number of presents
    total_presents = num_birthday_presents + num_christmas_presents
    result = total_presents
    return result

print(solution())