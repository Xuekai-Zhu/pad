def solution():
    """On Tuesday last week, Leo dropped off 10 pairs of trousers and some shirts at Sudsy Laundry. He was given a bill of $140, charged at $5 per shirt and $9 for each pair of trousers. When he went to pick up his clothes yesterday, the attendant insisted that he had only dropped off 2 shirts. Leo reported the matter to the manager, who ordered the attendant to search for the rest of Leo’s shirts. How many shirts were missing?"""
    total_trousers = 10
    total_cost = 140
    trouser_cost = 9
    shirt_cost = 5
    trouser_amount = total_trousers * trouser_cost
    shirt_amount = total_cost - trouser_amount
    actual_shirt_amount = (total_cost - (total_trousers * trouser_cost)) / shirt_cost
    missing_shirts = (total_shirts - actual_shirt_amount)
    result = missing_shirts
    return result

print(solution())