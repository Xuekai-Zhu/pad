def solution():
    """It costs Molly $5 per package to send Christmas gifts to her relatives by mail. She has two parents and three brothers, and each of her brothers is married with 2 children each. If she sends one package to each relative by mail, how much does it cost her to send all of the gifts by mail to her relatives, in dollars?"""
    num_parents = 2
    num_brothers = 3
    num_brother_spouses = 3
    num_nieces_nephews = 6
    total_recipients = num_parents + num_brothers + num_brother_spouses + num_nieces_nephews
    cost_per_package = 5
    total_cost = total_recipients * cost_per_package
    result = total_cost
    return result

print(solution())