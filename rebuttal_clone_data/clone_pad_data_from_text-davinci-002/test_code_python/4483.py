def solution():
     total_records = 200
     records_sold_to_sammy = total_records
     records_sold_to_bryan = total_records / 2
 
     profit_from_sammy = records_sold_to_sammy * 4
     profit_from_bryan = (records_sold_to_bryan * 6) + ((total_records - records_sold_to_bryan) * 1)
 
     difference_in_profit = profit_from_bryan - profit_from_sammy
     return difference_in_profit

print(solution())