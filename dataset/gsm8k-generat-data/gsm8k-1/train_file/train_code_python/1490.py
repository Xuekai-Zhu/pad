def solution():
    """Mr Julien's store has 400 marbles remaining after the previous day's sales. Twenty customers came into the store, and each bought 15 marbles. How many marbles remain in the store?"""
    starting_marbles = 400
    customers = 20
    marbles_per_customer = 15
    sold_marbles = customers * marbles_per_customer
    remaining_marbles = starting_marbles - sold_marbles
    result = remaining_marbles
    return result

print(solution())