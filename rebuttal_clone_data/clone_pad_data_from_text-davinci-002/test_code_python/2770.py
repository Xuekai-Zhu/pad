def solution():
     price_pizza = 10
     price_drinks = 2
     price_hamburger = 3
     
     Robert_pizza = 5
     Robert_drinks = 10
     Teddy_hamburger = 6
     Teddy_drinks = 10
     
     Robert_spend = Robert_pizza * price_pizza + Robert_drinks * price_drinks
     Teddy_spend = Teddy_hamburger * price_hamburger + Teddy_drinks * price_drinks
     
     total_spend = Robert_spend + Teddy_spend
     
     result = total_spend
     
     return result

print(solution())