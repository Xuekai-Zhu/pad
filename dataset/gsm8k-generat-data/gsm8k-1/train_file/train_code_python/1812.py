def solution():
    """Carrie harvested 200 tomatoes and 350 carrots on her farm. If she can sell a tomato for $1 and a carrot for $1.50, how much money can she make if she sells all of her tomatoes and carrots?"""
    tomatoes = 200
    carrots = 350
    tomato_price = 1
    carrot_price = 1.5
    revenue = (tomatoes*tomato_price) + (carrots*carrot_price)
    result = revenue
    return result

print(solution())