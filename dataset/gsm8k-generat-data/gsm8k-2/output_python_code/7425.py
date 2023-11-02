def solution():
    """We harvested 405 kg of apples. 90 kg were used to make fruit juice and 60 kg were given to a restaurant. The rest was sold in 5 kg bags and their sale brought in $408. What was the selling price of one bag of apples?"""
    total_apples = 405
    used_apples = 90 + 60
    remaining_apples = total_apples - used_apples
    bags_sold = remaining_apples / 5
    price_per_bag = 408 / bags_sold
    result = price_per_bag
    return result

print(solution())