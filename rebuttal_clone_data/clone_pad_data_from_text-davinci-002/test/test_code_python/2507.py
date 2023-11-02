def solution():
    bread_cost = 4.00
    meat_cost = 5.00
    cheese_cost = 4.00
    num_bread = 1
    num_meat = 2
    num_cheese = 2
    total_cost = (bread_cost * num_bread) + ((meat_cost * num_meat) - 1) + ((cheese_cost * num_cheese) - 1)
    cost_per_sandwich = total_cost / 10
    result = cost_per_sandwich
    return result

print(solution())