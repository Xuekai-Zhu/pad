def solution():
    bushels_grown = 50
    bushels_given_away = 8 + 3 + 12 + 21
    ears_per_bushel = 14
    total_ears = bushels_grown * ears_per_bushel
    ears_left = total_ears - bushels_given_away
    result = ears_left
    
    return result

print(solution())