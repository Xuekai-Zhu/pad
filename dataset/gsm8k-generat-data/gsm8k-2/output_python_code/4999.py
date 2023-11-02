def solution():
    """Ray buys a pack of hamburger meat for $5.00, a box of crackers for $3.50, 4 bags of frozen vegetables at $2.00 per bag and a pack of cheese for $3.50 at the grocery store. Because he is a store rewards member, he gets 10% off of his purchase. What does his total grocery bill come to?"""
    hamburger_meat_cost = 5.00
    crackers_cost = 3.50
    frozen_veggies_cost = 2.00
    cheese_cost = 3.50
    number_of_bags_of_frozen_veggies = 4
    total_cost = hamburger_meat_cost + crackers_cost + (frozen_veggies_cost * number_of_bags_of_frozen_veggies) + cheese_cost
    discount = total_cost * 0.1
    total_cost_after_discount = total_cost - discount
    result = total_cost_after_discount
    return result

print(solution())