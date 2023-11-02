def solution():
    
    starting_marbles = 400
    customers = 20
    marbles_per_customer = 15
    sold_marbles = customers * marbles_per_customer
    remaining_marbles = starting_marbles - sold_marbles
    result = remaining_marbles
    return result

print(solution())