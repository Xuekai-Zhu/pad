def solution():
     total_money = 50
     shirt_cost = 8
     key_chain_cost = 2
     bag_cost = 10
     money_spent = shirt_cost * 2 + bag_cost * 2
     money_left = total_money - money_spent
     key_chains_bought = money_left / key_chain_cost
     result = key_chains_bought
     return result

print(solution())