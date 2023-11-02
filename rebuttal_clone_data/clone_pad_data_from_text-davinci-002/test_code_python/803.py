def solution():
    vampire_students = 11
    pumpkin_students = 14
    vampire_packs = (vampire_students // 5) + (vampire_students % 5)
    pumpkin_packs = (pumpkin_students // 5) + (pumpkin_students % 5)
    vampire_cost = vampire_packs * 3
    pumpkin_cost = pumpkin_packs * 3
    individual_vampire_cost = vampire_students * 1
    individual_pumpkin_cost = pumpkin_students * 1
    total_cost = vampire_cost + pumpkin_cost + individual_vampire_cost + individual_pumpkin_cost
    result = total_cost
    
    return result

print(solution())