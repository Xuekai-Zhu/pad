def solution():
    ice_cream_cost = 2.00
    topping_cost = 0.50
    number_of_toppings = 10

    sundae_cost = ice_cream_cost + (number_of_toppings * topping_cost)
    result = sundae_cost
    return result

print(solution())