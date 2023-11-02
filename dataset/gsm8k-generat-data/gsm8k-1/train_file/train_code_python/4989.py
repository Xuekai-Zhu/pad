def solution():
    """On Tuesday last week, Leo dropped off 10 pairs of trousers and some shirts at Sudsy Laundry. He was given a bill of $140, charged at $5 per shirt and $9 for each pair of trousers. When he went to pick up his clothes yesterday, the attendant insisted that he had only dropped off 2 shirts. Leo reported the matter to the manager, who ordered the attendant to search for the rest of Leo’s shirts. How many shirts were missing?"""
    total_items = 10  # 10 pairs of trousers
    bill = 140
    trouser_price = 9
    shirt_price = 5

    total_trouser_cost = total_items * trouser_price
    total_shirt_cost = bill - total_trouser_cost
    missing_shirts = (total_shirt_cost / shirt_price) - 2

    result = missing_shirts

    return result

print(solution())