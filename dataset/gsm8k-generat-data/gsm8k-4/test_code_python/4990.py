def solution():
    """On Tuesday last week, Leo dropped off 10 pairs of trousers and some shirts at Sudsy Laundry. He was given a bill of $140, charged at $5 per shirt and $9 for each pair of trousers. When he went to pick up his clothes yesterday, the attendant insisted that he had only dropped off 2 shirts. Leo reported the matter to the manager, who ordered the attendant to search for the rest of Leo’s shirts. How many shirts were missing?"""
    # Define the number of pairs of trousers and the total bill
    trousers = 10
    total_bill = 140

    # Calculate the cost of the trousers
    trouser_cost = trousers * 9

    # Calculate the cost of the shirts
    shirt_cost = total_bill - trouser_cost

    # Calculate the number of shirts
    shirts = shirt_cost / 5

    # Calculate the number of missing shirts
    missing_shirts = 8 - shirts

    result = missing_shirts
    return result

print(solution())