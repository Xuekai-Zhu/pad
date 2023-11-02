def solution():
     chicken_feed = 20
     chicken_cost = 2
     chicken_profit = 1.50
     chickend_sold = 65 / chicken_profit
     total_feed_needed = chickend_sold * chicken_feed
     total_cost = total_feed_needed * chicken_cost
     final_profit = 65 - total_cost
     
 return final_profit

print(solution())