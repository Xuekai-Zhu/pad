def solution():
    """Gloria wants to buy the $129,000 mountain cabin that her friend Alfonso is selling. She only has $150 in cash. She intends to raise the remaining amount by selling her mature trees for lumber. She has 20 cypress trees, 600 pine trees, and 24 maple trees. She will get $100 for each cypress tree, $300 for a maple tree, and $200 per pine tree. After paying Alfonso for the cabin, how much money will Gloria have left?"""
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