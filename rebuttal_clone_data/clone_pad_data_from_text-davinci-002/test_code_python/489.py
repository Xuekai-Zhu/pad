def solution():
     top_price = 8
     abc_price = 23
     top_sales = 13
     abc_sales = 4
     top_earnings = top_price * top_sales
     abc_earnings = abc_price * abc_sales
     total_earnings = top_earnings + abc_earnings
     result = total_earnings
     return result

print(solution())