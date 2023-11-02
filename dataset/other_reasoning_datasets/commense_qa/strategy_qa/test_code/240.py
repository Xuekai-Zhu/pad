def solution():
    italian_food = "Pizza"
    pizza_toppings = ["Anchovies"]
    if all(topping in italian_food for topping in pizza_toppings):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())