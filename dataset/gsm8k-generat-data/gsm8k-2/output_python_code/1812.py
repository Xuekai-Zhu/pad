def solution():
    """Carrie harvested 200 tomatoes and 350 carrots on her farm. If she can sell a tomato for $1 and a carrot for $1.50, how much money can she make if she sells all of her tomatoes and carrots?"""
    tomato_price = 1
    carrot_price = 1.5
    total_tomato_income = tomato_price * 200
    total_carrot_income = carrot_price * 350
    total_income = total_tomato_income + total_carrot_income
    result = total_income
    return result

print(solution())