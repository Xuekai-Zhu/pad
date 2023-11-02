def solution():
    """Genevieve picked some cherries from the supermarket shelves that cost $8 per kilogram. When Genevieve reached the checkout counter, she realized she was $400 short of the total price and her friend Clarice chipped in. If Genevieve had $1600 on her, how many kilograms of cherries did she buy?"""
    cherry_price = 8
    genevieve_money = 1600
    total_cost = genevieve_money + 400
    cherries_bought = total_cost / cherry_price
    result = cherries_bought
    return result

print(solution())