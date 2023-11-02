def solution():
    
    credits = 14
    cost_per_credit = 450
    textbooks = 5
    cost_per_textbook = 120
    facilities_fee = 200
    total_cost = (credits * cost_per_credit) + (textbooks * cost_per_textbook) + facilities_fee
    result = total_cost
    return result

print(solution())