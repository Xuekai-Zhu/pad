def solution():
     sibling_gift_cost = 3 * 30
     total_gift_cost = 150
     parent_gift_cost = total_gift_cost - sibling_gift_cost
     result = parent_gift_cost / 2
     return result

print(solution())