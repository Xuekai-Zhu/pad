def solution():
    """Aleksandra went to a restaurant for dinner. She ordered some soup, a bagel, and a piece of cake. The bagel cost $4, and the soup 25% more. The cake is only half of the price of the bagel. How much did Aleksandra need to pay for the dinner she ordered?"""
    bagel_cost = 4
    soup_cost = bagel_cost * 1.25
    cake_cost = bagel_cost / 2
    total_cost = bagel_cost + soup_cost + cake_cost
    result = total_cost
    return result

print(solution())