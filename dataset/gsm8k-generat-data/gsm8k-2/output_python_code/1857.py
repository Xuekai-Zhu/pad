def solution():
    """Jill and Bob want to finally buy a house for themselves, so they went with a real estate agent to see some houses before making a decision. The first house was not too far from their work and the price was accessible. The second house was really big and Jill loved it but was twice as expensive as the first one and was way over their budget. They ended up buying the first one, knowing that the price of both houses altogether is $600,000. How much money did Jill and Bob end up paying for their new house?"""
    total_price = 600000
    second_house_price = total_price / 3
    first_house_price = total_price - second_house_price
    result = first_house_price
    return result

print(solution())