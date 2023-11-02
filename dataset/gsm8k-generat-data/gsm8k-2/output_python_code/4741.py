def solution():
    """It costs Molly $5 per package to send Christmas gifts to her relatives by mail. She has two parents and three brothers, and each of her brothers is married with 2 children each. If she sends one package to each relative by mail, how much does it cost her to send all of the gifts by mail to her relatives, in dollars?"""
    num_parents = 2
    num_brothers = 3
    num_brothers_spouses = num_brothers * 2
    num_nephews_nieces = num_brothers_spouses * 2
    total_relatives = num_parents + num_brothers + num_brothers_spouses + num_nephews_nieces
    cost_per_gift = 5
    total_cost = total_relatives * cost_per_gift
    result = total_cost
    return result

print(solution())