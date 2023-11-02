def solution():
 cookies_total = 30
 cookies_father = 10
 cookies_mother = cookies_father / 2
 cookies_brother = cookies_mother + 2
 cookies_left = cookies_total - (cookies_father + cookies_mother + cookies_brother)
 result = cookies_left
 return result

 Question: If Lisa buys 4 items at the store, each costing $2.79, what is the total cost of her purchase?
 Solution: 
 def solution():
     items_purchased = 4
     cost_per_item = 2.79
     total_cost = items_purchased * cost_per_item
     result = total_cost
     return result

print(solution())