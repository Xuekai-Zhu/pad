def solution():
    
    square_footage = 2000
    kitchen_cost = 20000
    bathroom_cost = 12000
    other_modules_cost = (square_footage - 400 - 2 * 150) * 100
    total_cost = kitchen_cost + 2 * bathroom_cost + other_modules_cost
    result = total_cost
    return result

print(solution())