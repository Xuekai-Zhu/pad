def solution():
    """Gloria wants to buy the $129,000 mountain cabin that her friend Alfonso is selling. She only has $150 in cash. She intends to raise the remaining amount by selling her mature trees for lumber. She has 20 cypress trees, 600 pine trees, and 24 maple trees. She will get $100 for each cypress tree, $300 for a maple tree, and $200 per pine tree. After paying Alfonso for the cabin, how much money will Gloria have left?"""

    # Define the price per tree
    CYPRESS_PRICE = 100
    PINE_PRICE = 200
    MAPLE_PRICE = 300

    # Define the number of trees Gloria wants to sell
    cypress_trees = 20
    pine_trees = 600
    maple_trees = 24

    # Calculate the total revenue from selling the trees
    revenue = (cypress_trees * CYPRESS_PRICE) + (pine_trees * PINE_PRICE) + (maple_trees * MAPLE_PRICE)

    # Calculate the amount of money Gloria will have left after paying Alfonso
    money_left = revenue + 150 - 129000

    # Display the amount of money Gloria will have left
    result = money_left
    return result

print(solution())