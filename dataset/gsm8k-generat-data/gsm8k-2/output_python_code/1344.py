def solution():
    """Mimi has decided to start going to the gym again. Over the weekend, she spent $8,000 on athletic sneakers and clothes. She spent thrice as much on Nike sneakers as she did on Adidas. What she spent on Adidas was 1/5 the cost of Skechers. If Mimi's Adidas sneakers purchase was $600, what amount did she spend on clothes?"""
    adidas_purchase = 600
    nike_purchase = adidas_purchase * 3
    skechers_purchase = adidas_purchase * 5
    total_sneaker_purchase = adidas_purchase + nike_purchase + skechers_purchase
    clothes_purchase = 8000 - total_sneaker_purchase
    result = clothes_purchase
    return result

print(solution())