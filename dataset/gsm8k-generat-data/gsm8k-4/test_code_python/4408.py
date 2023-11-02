def solution():
    """For every loaf of bread that Ted buys, he needs an additional 2 packs of sandwich meat and 2 packs of sliced cheese to make 10 sandwiches. The bread costs $4.00, the sandwich meat costs $5.00 per pack and the cheese costs $4.00 per pack. He has a $1.00 off coupon for one pack of cheese and an additional $1.00 coupon for one pack of meat. How much does each sandwich cost?"""
    # Define the cost of the bread and the amount of additional ingredients for 10 sandwiches
    bread_cost = 4
    meat_per_sandwich = 0.5
    cheese_per_sandwich = 0.5

    # Define the cost and coupon amount for the meat and cheese
    meat_cost = 5
    cheese_cost = 4
    meat_coupon = 1
    cheese_coupon = 1

    # Calculate the total cost of the ingredients for 10 sandwiches
    total_ingredient_cost = ((meat_per_sandwich * meat_cost) - meat_coupon + (cheese_per_sandwich * cheese_cost) - cheese_coupon)

    # Calculate the cost per sandwich by adding the cost of the bread and dividing by 10
    cost_per_sandwich = (bread_cost + total_ingredient_cost) / 10

    # Return the result
    result = round(cost_per_sandwich, 2)
    return result

print(solution())