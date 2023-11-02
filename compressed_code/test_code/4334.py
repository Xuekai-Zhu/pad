def solution():
    
    total_notes = 0
    total_notes += 2 * 100  
    total_notes += 1 * 50  
    total_notes += 5 * 20  
    total_notes += 3 * 10  
    total_notes += 7 * 5  
    total_notes += 27  
    coins = 0.0 
    total_money = total_notes + coins
    money_to_turn_in = total_money - 300
    result = money_to_turn_in
    return result

print(solution())