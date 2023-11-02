def solution():
     club_balance = 100
     player_sale_1 = 10
     player_sale_2 = 10
     total_money_in = club_balance + player_sale_1 + player_sale_2
     player_purchase_1 = 15
     player_purchase_2 = 15
     player_purchase_3 = 15
     player_purchase_4 = 15
     total_money_out = player_purchase_1 + player_purchase_2 + player_purchase_3 + player_purchase_4
     register_balance = total_money_in - total_money_out
     result = register_balance
     
     return result

print(solution())