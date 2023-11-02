def solution():
     bill_money = 30
     pizza_total = 11 * 3
     frank_money = pizza_total - bill_money
     bill_money = frank_money + bill_money
     result = bill_money
 
     return result

print(solution())