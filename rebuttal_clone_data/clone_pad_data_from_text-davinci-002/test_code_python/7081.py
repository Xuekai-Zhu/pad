def solution():
     purchase_one = 13
     purchase_two = 24
     budget_leftover = 6
     budget_given = 50
     total_budget = budget_leftover + budget_given
     total_spent = purchase_one + purchase_two
     budget_remaining = total_budget - total_spent
     result = budget_remaining
     return result

print(solution())