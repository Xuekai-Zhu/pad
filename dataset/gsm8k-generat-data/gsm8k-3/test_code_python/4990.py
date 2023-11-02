def solution():
    """On Tuesday last week, Leo dropped off 10 pairs of trousers and some shirts at Sudsy Laundry. He was given a bill of $140, charged at $5 per shirt and $9 for each pair of trousers. When he went to pick up his clothes yesterday, the attendant insisted that he had only dropped off 2 shirts. Leo reported the matter to the manager, who ordered the attendant to search for the rest of Leo’s shirts. How many shirts were missing?"""
    # Define the cost per shirt and per pair of trousers
    SHIRT_COST = 5
    TROUSERS_COST = 9

    # Define the total cost and the number of trousers dropped off
    total_cost = 140
    num_trousers = 10

    # Calculate the cost of the trousers
    trousers_cost = num_trousers * TROUSERS_COST

    # Calculate the cost of the missing shirts
    missing_shirts_cost = total_cost - trousers_cost - 2 * SHIRT_COST

    # Calculate the number of missing shirts
    missing_shirts = missing_shirts_cost // SHIRT_COST

    # Display the number of missing shirts
    result = missing_shirts
    return result

print(solution())