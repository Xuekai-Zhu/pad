def solution():
    
    total_cupcakes = 63
    chocolate_cupcakes = 8
    toffee_cupcakes = 40
    cupcakes_already_buyed = chocolate_cupcakes + toffee_cupcakes
    cupcakes_to_buyed = total_cupcakes - cupcakes_already_buyed
    result = cupcakes_to_buyed
    return result

print(solution())