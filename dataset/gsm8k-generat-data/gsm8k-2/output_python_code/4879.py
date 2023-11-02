def solution():
    """Jim and his Cousin are out at a restaurant. They each order a cheeseburger and milkshake. They also split an order to cheese fries. A cheeseburger is $3. A milkshake is $5. Cheese fries are $8. They spend 80% of their combined money. If Jim brought $20 how much did his cousin bring?"""
    jim_money = 20
    total_money = jim_money / 0.8
    jim_portion = 3 + 5 + 8/2  # cheeseburger + milkshake + half of cheese fries
    cousin_portion = (total_money * 0.8 - jim_portion) / 2
    result = cousin_portion
    return result

print(solution())