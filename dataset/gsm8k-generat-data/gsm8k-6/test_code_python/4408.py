def solution():
    # Calculate the total cost of the sandwich ingredients
    bread_cost = 4.00  # cost of one loaf of bread
    meat_cost = 5.00 - 1.00  # cost of one pack of sandwich meat after $1.00 off coupon
    cheese_cost = 4.00  # cost of one pack of sliced cheese
    cost_per_sandwich = (bread_cost + (2*meat_cost) + (2*cheese_cost))/10  # cost per sandwich

    result = cost_per_sandwich
    return result

print(solution())