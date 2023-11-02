def solution():
     lemonade_cost = 2 * 2
     sandwich_cost = 2 * 2.50
     total_cost = lemonade_cost + sandwich_cost
     bill = 20
     change_needed = bill - total_cost
     result = change_needed
     return result

print(solution())