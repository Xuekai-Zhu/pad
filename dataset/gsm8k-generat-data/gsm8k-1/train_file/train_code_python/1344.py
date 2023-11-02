def solution():
    """Mimi has decided to start going to the gym again. Over the weekend, she spent $8,000 on athletic sneakers and clothes. She spent thrice as much on Nike sneakers as she did on Adidas. What she spent on Adidas was 1/5 the cost of Skechers. If Mimi's Adidas sneakers purchase was $600, what amount did she spend on clothes?"""
    total_spent = 8000
    adidas_spent = 600
    nike_spent = adidas_spent * 3
    skechers_spent = adidas_spent * 5
    clothes_spent = total_spent - (adidas_spent + nike_spent + skechers_spent)
    result = clothes_spent
    return result

print(solution())