def solution():
    tip = 99
    steak_price = 24
    num_steaks = 2
    burger_price = 3.5
    num_burgers = 2
    ice_cream_price = 2
    num_ice_creams = 3

    # Calculate the total cost of all food items
    total_food_cost = (steak_price * num_steaks) + (burger_price * num_burgers) + (ice_cream_price * num_ice_creams)

    # Calculate the total amount spent, including the tip
    total_spent = total_food_cost + tip

    # Calculate how much money Selena will be left with
    starting_amount = total_spent + tip  # includes original tip amount
    final_amount = starting_amount - total_spent
    result = final_amount
    return result

print(solution())