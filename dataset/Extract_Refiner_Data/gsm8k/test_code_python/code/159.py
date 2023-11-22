def solution():
    
    # Define the cost of one red car
    RED_CAR_PRICE = 4

    # Define the number of red cars and action figures
    red_cars = 5
    action_figures = 3

    # Calculate the cost of one action figure
    action_figure_cost = RED_CAR_PRICE * red_cars + action_figures * action_figure_cost

    # Calculate the total cost of all toys
    total_cost = action_figure_cost + RED_CAR_PRICE * red_cars + action_figure_cost + DOLL_PRICE * 3

    # Display the total cost
    result = total_cost
    return result

print(solution())