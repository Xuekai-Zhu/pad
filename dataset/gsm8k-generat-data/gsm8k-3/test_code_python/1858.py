def solution():
    """Jill and Bob want to finally buy a house for themselves, so they went with a real estate agent to see some houses before making a decision. The first house was not too far from their work and the price was accessible. The second house was really big and Jill loved it but was twice as expensive as the first one and was way over their budget. They ended up buying the first one, knowing that the price of both houses altogether is $600,000. How much did Jill and Bob end up paying for their new house?"""
    # Define the total price of both houses
    total_price = 600000

    # Let x be the price of the first house
    # Then the price of the second house is 2x
    # We know that x + 2x = total_price
    # Solving for x, we get x = total_price / 3
    x = total_price / 3
    
    # Jill and Bob ended up buying the first house, which is priced at x
    result = x
    return result

print(solution())