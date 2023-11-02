def solution():
    num_red_cars = 5
    red_car_cost = 4

    num_action_figures = 3
    action_figures_cost = 4

    doll_cost = 3 * action_figures_cost

    # Calculate the total cost of all red cars
    total_red_car_cost = num_red_cars * red_car_cost

    # Calculate the total cost of all action figures
    total_action_figures_cost = num_action_figures * action_figures_cost

    # Calculate the total cost of all toys
    total_cost = total_red_car_cost + total_action_figures_cost + doll_cost
    result = total_cost
    return result

print(solution())