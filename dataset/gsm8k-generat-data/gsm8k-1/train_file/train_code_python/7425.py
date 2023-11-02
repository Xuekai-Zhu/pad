def solution():
    """We harvested 405 kg of apples. 90 kg were used to make fruit juice and 60 kg were given to a restaurant.
    The rest was sold in 5 kg bags and their sale brought in $408. What was the selling price of one bag of apples?"""
    total_apples = 405
    apples_used = 90 + 60
    apples_sold = total_apples - apples_used
    bags_sold = apples_sold / 5
    price_per_bag = 408 / bags_sold
    result = price_per_bag
    return result

print(solution())