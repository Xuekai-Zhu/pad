def solution():
    
    kitchen_cost = 20000
    bathroom_cost = 12000
    other_cost = 100
    total_area = 2000
    kitchen_area = 400
    bathroom_area = 150
    other_area = total_area - kitchen_area - (2 * bathroom_area)
    total_cost = (kitchen_cost + (2 * bathroom_cost) + (other_area * other_cost))
    result = total_cost
    return result

print(solution())