def solution():
    # Calculate the total cost of the sandwich meat and cheese
    meat_cost = 5.00 - 1.00  # One pack of sandwich meat costs $5.00, but he has a $1.00 coupon
    cheese_cost = 4.00 - 1.00  # One pack of sliced cheese cost $4.00, but he has a $1.00 coupon
    total_filling_cost = (2 * meat_cost) + (2 * cheese_cost)  # Ted needs 2 packs of meat and 2 packs of cheese for 10 sandwiches

    # Calculate the total cost of all the ingredients
    bread_cost = 4.00  # The bread costs $4.00 per loaf
    total_cost = bread_cost + total_filling_cost

    # Calculate the cost per sandwich
    sandwiches_per_loaf = 10  # Ted can make 10 sandwiches with one loaf of bread
    cost_per_sandwich = total_cost / sandwiches_per_loaf
    result = cost_per_sandwich
    return result

print(solution())