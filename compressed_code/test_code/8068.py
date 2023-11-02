def solution():
    
    cabin_price = 129000
    cash = 150
    cypress_trees = 20
    maple_trees = 24
    pine_trees = 600
    cypress_value = 100
    maple_value = 300
    pine_value = 200
    
    total_tree_value = (cypress_trees * cypress_value) + (maple_trees * maple_value) + (pine_trees * pine_value)
    gloria_money = total_tree_value - (cabin_price - cash)
    result = gloria_money
    return result

print(solution())