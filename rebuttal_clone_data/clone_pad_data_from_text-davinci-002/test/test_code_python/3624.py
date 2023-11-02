def solution():
     friend_gifts = 8
     gift_price = 9
     total_budget = 100
     leftover_budget = total_budget - (friend_gifts * gift_price)
     parents_gift_budget = leftover_budget / 2
     result = parents_gift_budget
     return result

print(solution())