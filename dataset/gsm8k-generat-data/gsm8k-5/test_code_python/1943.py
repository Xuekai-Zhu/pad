def solution():
    num_children = 4
    num_parents = 2
    num_grandparents = 1
    cost_per_person = 5  # $5 for entrance ticket
    cost_per_child = 2  # $2 for each child's attraction ticket
    cost_per_parent = 4  # $4 for each parent's attraction ticket
    num_attractions = 1  # Visiting one attraction

    # Calculate the total cost for the entrance tickets
    total_entrance_cost = (num_children + num_parents + num_grandparents) * cost_per_person

    # Calculate the total cost for visiting one attraction
    total_attraction_cost = (num_children * cost_per_child + num_parents * cost_per_parent) * num_attractions

    # Calculate the total cost for the whole visit
    total_cost = total_entrance_cost + total_attraction_cost
    result = total_cost
    return result

print(solution())