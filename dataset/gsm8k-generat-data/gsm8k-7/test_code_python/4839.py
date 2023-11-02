def solution():
    num_cupcakes = 12
    cost_per_cupcake = 1.5
    total_cost = num_cupcakes * cost_per_cupcake
    cost_per_person = total_cost / 2  # split evenly between 2 people
    result = cost_per_person
    return result

print(solution())