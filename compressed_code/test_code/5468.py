def solution():
    
    ticket1_cost = 150
    ticket2_cost = 150
    ticket3_cost = ticket1_cost / 3
    total_cost = ticket1_cost + ticket2_cost + ticket3_cost
    roommate_share = total_cost / 2
    total_cost -= roommate_share
    remaining_money = 500 - total_cost
    result = remaining_money
    return result

print(solution())