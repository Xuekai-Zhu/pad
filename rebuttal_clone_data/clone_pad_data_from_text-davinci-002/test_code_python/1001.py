def solution():
     orchids_sold = 20
     orchids_price = 50
     chinese_money_plants_sold = 15
     chinese_money_plants_price = 25
     workers_paid = 2 * 40
     new_pots_bought = 150
     total_earnings = orchids_sold * orchids_price + chinese_money_plants_sold * chinese_money_plants_price
     money_left = total_earnings - workers_paid - new_pots_bought
     result = money_left
     
     return result

print(solution())