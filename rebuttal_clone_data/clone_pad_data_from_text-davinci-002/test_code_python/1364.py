def solution():
     cost_per_credit = 450
     num_credits = 14
     textbooks = 5
     cost_per_textbook = 120
     facilities_fee = 200
     total_cost = cost_per_credit * num_credits + cost_per_textbook * textbooks + facilities_fee
     result = total_cost
     return result

print(solution())