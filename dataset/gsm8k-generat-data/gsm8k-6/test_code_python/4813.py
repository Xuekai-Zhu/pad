def solution():
    # Calculate the cost of window treatments for 3 windows
    num_sheers = 3  # number of pairs of sheers needed
    num_drapes = 3  # number of pairs of drapes needed
    cost_sheers = 40 * num_sheers  # cost of sheers for 3 windows
    cost_drapes = 60 * num_drapes  # cost of drapes for 3 windows
    total_cost = cost_sheers + cost_drapes  # total cost of window treatments for 3 windows
    result = total_cost
    return result

print(solution())