def solution():
    # Define the cost of each season pass
    pass_cost = 100.0
    
    # Define the number of times each son visited the park
    oldest_son_visits = 35
    youngest_son_visits = 15
    
    # Calculate the total cost for both passes
    total_cost = 2 * pass_cost
    
    # Calculate the total number of visits
    total_visits = oldest_son_visits + youngest_son_visits
    
    # Calculate the cost per visit
    cost_per_visit = total_cost / total_visits
    
    result = cost_per_visit
    return result

print(solution())