def solution():
     Peter_total = 62
     Jessica_total = 20
     Peter_shirts = 5
     Jessica_shirts = 2
     Peter_pants = 2
     price_per_shirt = (Peter_total - (Peter_pants * price_per_pair_of_pants)) / Peter_shirts
     price_per_pair_of_pants = (Jessica_total - (Jessica_shirts * price_per_shirt)) / Peter_pants
     result = price_per_pair_of_pants
     return result

print(solution())