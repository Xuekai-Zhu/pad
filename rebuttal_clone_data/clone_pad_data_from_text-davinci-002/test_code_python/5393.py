def solution():
    kitchen_module_cost = 20000
    bathroom_module_cost = 12000
    kitchen_module_size = 400
    bathroom_module_size = 150
    other_module_cost = 100
    other_module_size = 2000 - (kitchen_module_size + (2 * bathroom_module_size))
    total_cost = kitchen_module_cost + (2 * bathroom_module_cost) + (other_module_cost * other_module_size)
    result = total_cost
    return result

print(solution())