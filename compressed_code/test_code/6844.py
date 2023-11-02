def solution():
    
    total_spent = 8000
    adidas_spent = 600
    nike_spent = adidas_spent * 3
    skechers_spent = adidas_spent * 5
    clothes_spent = total_spent - (adidas_spent + nike_spent + skechers_spent)
    result = clothes_spent
    return result

print(solution())