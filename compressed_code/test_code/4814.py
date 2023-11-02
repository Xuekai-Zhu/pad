def solution():
    
    num_people = 4
    sandwiches_cost = 5
    fruit_salad_cost = 3
    sodas_cost = 2
    snacks_cost = 4
    sandwiches_count = num_people
    fruit_salad_count = num_people
    sodas_count = num_people * 2
    snacks_count = 3
    total_cost = (sandwiches_count * sandwiches_cost) + (fruit_salad_count * fruit_salad_cost) + (sodas_count * sodas_cost) + (snacks_count * snacks_cost)
    result = total_cost
    return result

print(solution())