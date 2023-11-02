def solution():
    
    total_pizzas = 4 * 4  
    bill_pizzas = 4 * 0.5  
    dale_pizzas = 4 * 0.5  
    ann_pizzas = 4 * 0.75  
    cate_pizzas = 4 * 0.75  
    total_eaten = bill_pizzas + dale_pizzas + ann_pizzas + cate_pizzas
    uneaten_pizzas = total_pizzas - total_eaten
    result = uneaten_pizzas
    return result

print(solution())