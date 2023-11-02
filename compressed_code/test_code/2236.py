def solution():
    
    cabin_price = 129000
    cash_on_hand = 150
    cypress_trees = 20
    pine_trees = 600
    maple_trees = 24
    cypress_price = 100
    pine_price = 200
    maple_price = 300
    total_tree_income = (cypress_trees * cypress_price) + (pine_trees * pine_price) + (maple_trees * maple_price)
    total_income = cash_on_hand + total_tree_income
    money_left = total_income - cabin_price
    result = money_left
    return result

print(solution())