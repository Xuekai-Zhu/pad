def solution():
     """Alexis is applying for a new job and bought a new set of business clothes to wear to the interview. She went to a department store with a budget of $200 and spent $30 on a button-up shirt, $46 on suit pants, $38 on a suit coat, $11 on socks, and $18 on a belt. She also purchased a pair of shoes, but lost the receipt for them. She has $16 left from her budget. How much did Alexis pay for the shoes?"""
     shirt_cost = 30
     pants_cost = 46
     coat_cost = 38
     socks_cost = 11
     belt_cost = 18
     budget = 200
     money_left = budget - (shirt_cost + pants_cost + coat_cost + socks_cost + belt_cost)
     shoes_cost = money_left
     result = shoes_cost
     return result

print(solution())