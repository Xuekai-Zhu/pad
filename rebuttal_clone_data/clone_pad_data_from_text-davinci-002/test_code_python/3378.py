def solution():
     eggs_sold = 120
     price_per_dozen = 3
     number_of_dozen_sold = eggs_sold / price_per_dozen
     eggs_laid = number_of_dozen_sold * 12
     hens = 10
     eggs_per_hen_per_week = eggs_laid / hens
 
     return eggs_per_hen_per_week

print(solution())