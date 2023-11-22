def solution():
    
    base_burrito = 6.5
    extra_meat = 2
    extra_cheese = 1
    avocado = 1
    sauces = 2
    sauces_price = 0.25
    upgrade_meal = 3
    gift_card = 5
    total_spent = base_burrito + extra_meat + extra_cheese + avocado + sauces
    total_spent -= upgrade_meal
    total_spent -= gift_card
    result = total_spent
    return result

print(solution())