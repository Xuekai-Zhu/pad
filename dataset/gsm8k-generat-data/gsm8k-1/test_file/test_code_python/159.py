def solution():
    """In a room, there are various toys: 5 red cars, 3 action figures, and a doll. The doll cost as much as 3 action figures and one red car cost $4. How much are all toys worth, of an action figure costs $5?"""
    red_cars = 5
    action_figures = 3
    doll = 1
    
    # Calculate the cost of one red car
    one_red_car = 4
    
    # Calculate the cost of one action figure
    one_action_figure = 5
    
    # Calculate the cost of one doll
    doll_cost = 3 * one_action_figure
    
    # Calculate the total cost of all toys
    total_cost = (red_cars * one_red_car) + (action_figures * one_action_figure) + doll_cost
    
    result = total_cost
    return result

print(solution())