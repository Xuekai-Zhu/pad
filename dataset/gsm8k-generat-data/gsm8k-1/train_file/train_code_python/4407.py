def solution():
    """For every loaf of bread that Ted buys, he needs an additional 2 packs of sandwich meat and 2 packs of sliced cheese to make 10 sandwiches. The bread costs $4.00, the sandwich meat costs $5.00 per pack and the cheese costs $4.00 per pack. He has a $1.00 off coupon for one pack of cheese and an additional $1.00 coupon for one pack of meat. How much does each sandwich cost?"""
    bread_cost = 4
    meat_cost = 5
    cheese_cost = 4
    cheese_discount = 1
    meat_discount = 1
    total_packs = 2 + 2
    total_sandwiches = 10
    total_cost = (bread_cost + meat_cost + cheese_cost) - cheese_discount - meat_discount
    cost_per_sandwich = total_cost / total_sandwiches
    result = cost_per_sandwich
    return result

print(solution())