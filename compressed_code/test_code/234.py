def solution():
    
    num_robots = 7
    robot_cost = 8.75
    tax = 7.22
    total_cost = (num_robots * robot_cost) + tax
    starting_money = total_cost + 11.53
    result = starting_money
    return result

print(solution())