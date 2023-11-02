def solution():
    
    gift_money = 50
    cost_of_tape = 9
    num_of_tapes = 2
    cost_of_headphone = 25
    total_cost = (cost_of_tape * num_of_tapes) + cost_of_headphone
    money_left = gift_money - total_cost
    result = money_left
    return result

print(solution())