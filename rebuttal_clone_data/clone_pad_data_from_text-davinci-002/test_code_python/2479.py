def solution():
     packets_of_chips = 15
     price_of_chips = 2
     price_of_corn_chips = 1.5
     money_spent_on_chips = packets_of_chips * price_of_chips
     money_left = 45 - money_spent_on_chips
     packets_of_corn_chips = money_left / price_of_corn_chips
     result = packets_of_corn_chips
 
     return result

print(solution())