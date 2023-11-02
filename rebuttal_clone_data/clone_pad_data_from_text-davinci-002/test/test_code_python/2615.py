def solution():
     chickens = 10
     eggs_laid_per_chicken_per_week = 6
     eggs_laid_per_week = chickens * eggs_laid_per_chicken_per_week
     weeks = 2
     eggs_laid = eggs_laid_per_week * weeks
     eggs_per_dozen = 12
     dozens_sold = eggs_laid / eggs_per_dozen
     price_per_dozen = 2
     total_sales = dozens_sold * price_per_dozen
     result = total_sales
     return result

print(solution())