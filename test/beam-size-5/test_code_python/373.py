def solution():
    
    monday_apples = 56
    tuesday_apples = 12
    wednesday_apples = monday_apples * 2
    total_apples = monday_apples + tuesday_apples + wednesday_apples
    price_per_piece = 4
    total_apples_picked = total_apples * price_per_piece
    result = total_apples_picked
    return result

print(solution())