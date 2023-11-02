def solution():
     """A craft store makes a third of its sales in the fabric section, a quarter of its sales in the jewelry section, and the rest in the stationery section. They made 36 sales today. How many sales were in the stationery section?"""
     total_sales = 36
     fabric_sales = total_sales / 3
     jewelry_sales = total_sales / 4
     stationery_sales = total_sales - (fabric_sales + jewelry_sales)
     result = stationery_sales
     
     return result

print(solution())