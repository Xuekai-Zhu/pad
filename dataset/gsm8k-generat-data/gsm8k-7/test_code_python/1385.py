def solution():
    backyard_sides = 9
    backyard_back = 18
    shared_side = (backyard_sides + backyard_back) / 2
    neighbor_back_pay = 0.5
    neighbor_left_pay = 1/3
    fence_cost = 3

    # Calculate the cost of the side shared with the neighbor behind
    shared_back_cost = shared_side * neighbor_back_pay * fence_cost

    # Calculate the cost of the side shared with the neighbor on the left
    shared_left_cost = backyard_sides * (1/3) * fence_cost

    # Calculate the total cost of all three sides
    total_cost = (backyard_sides + backyard_back + shared_side) * fence_cost - shared_back_cost - shared_left_cost
    result = total_cost
    return result

print(solution())