def solution():
    
    monday_quantity = 15
    tuesday_quantity = 3 * monday_quantity
    wednesday_quantity = 4 * tuesday_quantity
    total_quantity = monday_quantity + tuesday_quantity + wednesday_quantity
    result = total_quantity
    return result

print(solution())