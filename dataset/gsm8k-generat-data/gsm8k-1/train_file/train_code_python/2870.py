def solution():
    """Gloria wants to buy the $129,000 mountain cabin that her friend Alfonso is selling. 
    She only has $150 in cash. She intends to raise the remaining amount by selling 
    her mature trees for lumber. She has 20 cypress trees, 600 pine trees, and 24 maple 
    trees. She will get $100 for each cypress tree, $300 for a maple tree, and $200 per 
    pine tree. After paying Alfonso for the cabin, how much money will Gloria have left?"""
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