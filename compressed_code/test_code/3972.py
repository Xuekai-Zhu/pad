def solution():
    
    grapes = 100
    strawberries = (3/5) * grapes
    total_fruits = grapes + strawberries
    each_friend_share = 1/5 * total_fruits

    karlee_remaining = total_fruits - (each_friend_share * 2)
    result = karlee_remaining
    return result

print(solution())