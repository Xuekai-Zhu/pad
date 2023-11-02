def solution():
    """Ray buys a pack of hamburger meat for $5.00, a box of crackers for $3.50, 4 bags of frozen vegetables at $2.00 per bag and a pack of cheese for $3.50 at the grocery store. Because he is a store rewards member, he gets 10% off of his purchase. What does his total grocery bill come to?"""
    meat_cost = 5.00
    crackers_cost = 3.50
    vegetables_cost = 2.00 * 4
    cheese_cost = 3.50
    total_cost = meat_cost + crackers_cost + vegetables_cost + cheese_cost
    discount = total_cost * 0.10
    final_cost = total_cost - discount
    result = final_cost
    return result

print(solution())