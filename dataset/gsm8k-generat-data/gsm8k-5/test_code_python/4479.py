def solution():
    total_bushels = 50  # Bob grew 50 bushels of corn
    bushels_given_away = 8 + 3 + 12  # Bob gave away a total of 8+3+12 = 23 bushels
    bushels_remaining = total_bushels - bushels_given_away  # Calculate the remaining bushels

    # Calculate the number of ears of corn left
    ears_remaining = bushels_remaining * 14
    ears_remaining += 21  # Add the ears of corn accepted by Stacy
    result = ears_remaining
    return result

print(solution())