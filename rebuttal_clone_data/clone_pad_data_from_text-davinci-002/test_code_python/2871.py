def solution():
    cabin_price = 129000
    cash = 150
    cypress_trees = 20
    maple_trees = 24
    pine_trees = 600
    cypress_price = 100
    maple_price = 300
    pine_price = 200
    total_sale = (cypress_trees * cypress_price) + (maple_trees * maple_price) + (pine_trees * pine_price)
    money_left = total_sale - cabin_price
    result = money_left
    return result

print(solution())