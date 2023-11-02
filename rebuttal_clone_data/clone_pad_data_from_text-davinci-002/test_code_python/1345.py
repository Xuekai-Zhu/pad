def solution():
     nike_sneakers = 80000 / 3
     adidas_sneakers = 80000 / 15
     skechers_sneakers = 80000 / 5
     total_sneakers = nike_sneakers + adidas_sneakers + skechers_sneakers
     clothes_purchase = total_sneakers - adidas_sneakers
     
     return clothes_purchase

print(solution())