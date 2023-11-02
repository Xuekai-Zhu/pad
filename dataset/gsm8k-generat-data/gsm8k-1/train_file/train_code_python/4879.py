def solution():
    """Jim and his Cousin are out at a restaurant. They each order a cheeseburger and milkshake. They also split an order to cheese fries. A cheeseburger is $3. A milkshake is $5. Cheese fries are $8. They spend 80% of their combined money. If Jim brought $20, how much did his cousin bring?"""
    jim_money = 20
    total_spent = jim_money / 0.8
    total_cost = (3 + 5 + 8) * 2
    cousin_money = total_spent - jim_money
    result = cousin_money
    return result

print(solution())