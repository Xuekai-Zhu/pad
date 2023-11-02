def solution():
     pants_cost = 140
     shirt_cost = 43
     tie_cost = 15
     total_cost = pants_cost + shirt_cost + tie_cost
     bill_paid = 200
     change_due = bill_paid - total_cost
     result = change_due
     return result

print(solution())