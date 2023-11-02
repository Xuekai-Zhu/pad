def solution():
    
    num_sailors = 17
    num_inexperienced = 5
    inexperienced_pay = 10 * 60  
    experienced_pay = (6 / 5) * inexperienced_pay  
    num_experienced = num_sailors - num_inexperienced
    total_experienced_pay = num_experienced * experienced_pay * 4  
    result = total_experienced_pay
    return result

print(solution())