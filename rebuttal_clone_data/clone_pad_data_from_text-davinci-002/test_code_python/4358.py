def solution():
    children = 20
    pizzas = 5
    slices_per_pizza = [6, 8, 10]
    possible_solutions = []
    
    for i in range(len(slices_per_pizza)):
        if children%slices_per_pizza[i] == 0 and pizzas%children == 0:
            possible_solutions.append(slices_per_pizza[i])
    
    result = min(possible_solutions)
    
    return result

print(solution())