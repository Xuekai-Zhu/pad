def solution():
    cover_charge = 20
    friend_cover_charge = cover_charge * 2
    friend_drinks = 6 * 6
    friend_food = 14
    total_spent = friend_cover_charge + friend_drinks + friend_food
    tip = total_spent * 0.3
    total_spent_with_tip = total_spent + tip
    result = total_spent_with_tip
    
    return result

print(solution())