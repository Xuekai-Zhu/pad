def solution():
     total_cantaloupes = 30
     total_honeydews = 27
     dropped_cantaloupes = 2
     rotten_honeydews = 3
     cantaloupe_price = 2
     honeydew_price = 3
     final_cantaloupes = total_cantaloupes - dropped_cantaloupes - rotten_honeydews
     final_honeydews = total_honeydews - rotten_honeydews
     cantaloupe_sales = final_cantaloupes * cantaloupe_price
     honeydew_sales = final_honeydews * honeydew_price
     sales_total = cantaloupe_sales + honeydew_sales
     
     return sales_total

print(solution())